#!/usr/bin/env python
"""
Checker of generated packages.

- [x] import generated package
- [x] flake8
- [x] pyright
- [x] mypy
"""
import argparse
import json
import logging
import subprocess
import sys
import tempfile
from typing import List
from dataclasses import dataclass
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.resolve()
LOGGER_NAME = "check_output"
IGNORE_PYRIGHT_ERRORS = (
    '"get_paginator" is marked as overload, but no implementation is provided',
    '"get_waiter" is marked as overload, but no implementation is provided',
    # 'Expected type arguments for generic class "ResourceCollection"',
    # 'Type "None" cannot be assigned to type',
    # '"__next__" is not present',
    # 'Import "boto3.s3.transfer" could not be resolved',
    # "is partially unknown",
    'Method "paginate" overrides class "Paginator" in an incompatible manner',
    'Method "wait" overrides class "Waiter" in an incompatible manner',
    'define variable "items" in incompatible way',
    'define variable "values" in incompatible way',
    "must return value",
)
IGNORE_MYPY_ERRORS = (
    'Signature of "paginate" incompatible with supertype "Paginator"',
    'Signature of "wait" incompatible with supertype "Waiter"',
    "note:",
)


class SnapshotMismatchError(Exception):
    """
    Main snapshot mismatch exception.
    """


def setup_logging(level: int) -> logging.Logger:
    """
    Get Logger instance.

    Arguments:
        level -- Log level

    Returns:
        Overriden Logger.
    """
    logger = logging.getLogger(LOGGER_NAME)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(message)s", datefmt="%H:%M:%S")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)
    logger.addHandler(stream_handler)
    logger.setLevel(level)
    return logger


@dataclass
class CLINamespace:
    """
    CLI namespace.
    """

    debug: bool
    path: Path
    services: List[str]


def parse_args() -> CLINamespace:
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser(__file__)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-p", "--path", type=Path, default=ROOT_PATH / "mypy_boto3_output")
    parser.add_argument("services", nargs="*")
    args = parser.parse_args()
    return CLINamespace(
        debug=args.debug,
        path=args.path,
        services=args.services,
    )


def run_flake8(path: Path) -> None:
    """
    Check output with flake8.
    """
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "flake8",
                    "--ignore",
                    "E203,W503,E501,D200,D107,D401,D105,D205,D400,D101,D102,D403",
                    path.as_posix(),
                ],
                stderr=f,
                stdout=f,
            )
        except subprocess.CalledProcessError:
            temp_path = Path(f.name)
            output = temp_path.read_text()
            raise SnapshotMismatchError(output)


def run_pyright(path: Path) -> None:
    """
    Check output with pyright.
    """
    with tempfile.NamedTemporaryFile("w+b") as f:
        try:
            subprocess.check_call(
                ["npx", "pyright", path.as_posix(), "--outputjson"],
                stderr=subprocess.DEVNULL,
                stdout=f,
            )
            return
        except subprocess.CalledProcessError:
            pass

        temp_path = Path(f.name)
        output = temp_path.read_text()

        data = json.loads(output).get("generalDiagnostics", [])
        errors = []
        for error in data:
            message = error.get("message", "")
            if any(imsg in message for imsg in IGNORE_PYRIGHT_ERRORS):
                continue
            errors.append(error)

        if errors:
            messages = []
            for error in errors:
                messages.append(
                    f'{error["file"]}:{error["range"]["start"]["line"]} {error.get("message", "")}'
                )
            raise SnapshotMismatchError("\n".join(messages))


def run_mypy(path: Path) -> None:
    """
    Check output with mypy.
    """
    try:
        output = subprocess.check_output(
            [sys.executable, "-m", "mypy", path.as_posix()],
            stderr=subprocess.STDOUT,
            encoding="utf8",
        )
    except subprocess.CalledProcessError as e:
        output = e.output
        errors = []
        for message in output.splitlines():
            if not message or message.startswith("Found"):
                continue
            if any(imsg in message for imsg in IGNORE_MYPY_ERRORS):
                continue
            errors.append(message)

        if errors:
            raise SnapshotMismatchError("\n".join(errors)) from None


def run_call(path: Path) -> None:
    """
    Check output by running it.
    """
    try:
        print([sys.executable, path.as_posix()])
        subprocess.check_call([sys.executable, path.as_posix()], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(f"Path {path} cannot be imported: {e}") from None


def run_import(path: Path) -> None:
    """
    Check output by installing and importing it.
    """
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--no-input", path.parent.as_posix()],
            stdout=subprocess.DEVNULL,
        )
        subprocess.check_call(
            [sys.executable, "-c", f"import {path.name}"],
            stdout=subprocess.DEVNULL,
        )
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "--no-input", "-y", path.name],
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise SnapshotMismatchError(f"Path {path} cannot be imported: {e}") from None


def is_package_dir(path: Path) -> bool:
    """
    Check whether `path` contains a service package.
    """
    if not path.is_dir():
        return False
    if path.name.endswith(".egg-info"):
        return False
    if path.name.startswith("mypy_boto3_"):
        return True
    if path.name.startswith("types_aiobotocore_"):
        return True
    return False


def check_snapshot(path: Path) -> None:
    """
    Check package type checkers snapshot.

    Raises:
        SnapshotMismatchError -- If snapshot is not equal to current output.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(f"Running call for {path.name} ...")
    run_call(path)
    logger.debug(f"Running mypy for {path.name} ...")
    run_mypy(path)
    logger.debug(f"Running flake8 for {path.name} ...")
    run_flake8(path)
    logger.debug(f"Running pyright for {path.name} ...")
    run_pyright(path)
    logger.debug(f"Running import for {path.name} ...")
    run_import(path)


def main() -> None:
    """
    Run main logic.
    """
    args = parse_args()
    logger = setup_logging(logging.DEBUG if args.debug else logging.INFO)
    has_errors = False
    for folder in sorted(args.path.iterdir()):
        if not folder.name.endswith("_package"):
            continue
        for package_path in folder.iterdir():
            if not is_package_dir(package_path):
                continue
            if args.services and not any(s in package_path.name for s in args.services):
                continue
            logger.info(f"Checking {package_path.name} ...")
            try:
                check_snapshot(package_path)
            except SnapshotMismatchError as e:
                logger.error(e)
                has_errors = True

    if has_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
