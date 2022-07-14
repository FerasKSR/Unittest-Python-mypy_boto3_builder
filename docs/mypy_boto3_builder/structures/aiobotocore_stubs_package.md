# AioBotocoreStubsPackage

> Auto-generated documentation for [mypy_boto3_builder.structures.aiobotocore_stubs_package](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py) module.

Structure for types-aiobotocore module.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / AioBotocoreStubsPackage
    - [AioBotocoreStubsPackage](#aiobotocorestubspackage)
        - [AioBotocoreStubsPackage().essential_service_names](#aiobotocorestubspackageessential_service_names)
        - [AioBotocoreStubsPackage().get_all_names](#aiobotocorestubspackageget_all_names)
        - [AioBotocoreStubsPackage().get_session_required_import_records](#aiobotocorestubspackageget_session_required_import_records)

## AioBotocoreStubsPackage

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L18)

```python
class AioBotocoreStubsPackage(Package):
    def __init__(
        data: type[BasePackageData],
        session_class: ClassRecord | None = None,
        service_names: Iterable[ServiceName] = tuple(),
        service_packages: Iterable[ServicePackage] = tuple(),
        init_functions: Iterable[Function] = tuple(),
    ):
```

Structure for types-aiobotocore module.

#### See also

- [BasePackageData](../package_data.md#basepackagedata)
- [Function](function.md#function)
- [Package](package.md#package)
- [ServiceName](../service_name.md#servicename)
- [ServicePackage](service_package.md#servicepackage)

### AioBotocoreStubsPackage().essential_service_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L37)

```python
@property
def essential_service_names() -> list[ServiceName]:
```

Service names marked as essential.

#### See also

- [ServiceName](../service_name.md#servicename)

### AioBotocoreStubsPackage().get_all_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L90)

```python
def get_all_names() -> list[str]:
```

Get names for `__all__` directive.

### AioBotocoreStubsPackage().get_session_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/aiobotocore_stubs_package.py#L48)

```python
def get_session_required_import_records() -> list[ImportRecord]:
```

Get import reciords for `session.py[i]`.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)
