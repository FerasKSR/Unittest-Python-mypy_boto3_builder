# Version

> Auto-generated documentation for [mypy_boto3_builder.utils.version](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py) module.

Version-related utils.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Utils](index.md#utils) / Version
    - [get_aioboto3_version](#get_aioboto3_version)
    - [get_aiobotocore_version](#get_aiobotocore_version)
    - [get_boto3_version](#get_boto3_version)
    - [get_botocore_version](#get_botocore_version)
    - [get_builder_version](#get_builder_version)
    - [get_max_build_version](#get_max_build_version)
    - [get_min_build_version](#get_min_build_version)

## get_aioboto3_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L63)

```python
def get_aioboto3_version() -> str:
```

Get aioboto3 package version.

## get_aiobotocore_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L52)

```python
def get_aiobotocore_version() -> str:
```

Get aiobotocore package version.

## get_boto3_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L45)

```python
def get_boto3_version() -> str:
```

Get boto3 package version.

## get_botocore_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L38)

```python
def get_botocore_version() -> str:
```

Get botocore package version.

## get_builder_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L13)

```python
def get_builder_version() -> str:
```

Get program version.

## get_max_build_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L31)

```python
def get_max_build_version(version: str) -> str:
```

Get min version build version by bumping minor.

## get_min_build_version

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/utils/version.py#L24)

```python
def get_min_build_version(version: str) -> str:
```

Get min version build version by setting micro to 0.
