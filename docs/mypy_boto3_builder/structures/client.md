# Client

> Auto-generated documentation for [mypy_boto3_builder.structures.client](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py) module.

Boto3 Client.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Client
    - [Client](#client)
        - [Client().\_\_hash\_\_](#client__hash__)
        - [Client().boto3_doc_link](#clientboto3_doc_link)
        - [Client().get_all_names](#clientget_all_names)
        - [Client.get_class_name](#clientget_class_name)
        - [Client().get_example_method](#clientget_example_method)
        - [Client().get_exceptions_property](#clientget_exceptions_property)
        - [Client().get_required_import_records](#clientget_required_import_records)
        - [Client().own_methods](#clientown_methods)

## Client

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L22)

```python
class Client(ClassRecord):
    def __init__(
        name: str,
        service_name: ServiceName,
        boto3_client: BaseClient,
    ) -> None:
```

Boto3 Client.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [ServiceName](../service_name.md#servicename)

### Client().\_\_hash\_\_

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L58)

```python
def __hash__() -> int:
```

Calculate hash from client service name.

### Client().boto3_doc_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L71)

```python
@property
def boto3_doc_link() -> str:
```

List to boto3 docs page.

### Client().get_all_names

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L78)

```python
def get_all_names() -> list[str]:
```

Get a list of names for `__all__` statement.

### Client.get_class_name

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L64)

```python
@staticmethod
def get_class_name(service_name: ServiceName) -> str:
```

Get class name for ServiceName.

#### See also

- [ServiceName](../service_name.md#servicename)

### Client().get_example_method

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L120)

```python
def get_example_method() -> Method | None:
```

Get a nice method with return TypedDict for documentation.

### Client().get_exceptions_property

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L93)

```python
def get_exceptions_property() -> Method:
```

Generate Client exceptions property.

#### See also

- [Method](method.md#method)

### Client().get_required_import_records

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L112)

```python
def get_required_import_records() -> set[ImportRecord]:
```

Extract import records from required type annotations.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### Client().own_methods

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/client.py#L84)

```python
@property
def own_methods() -> Iterator[Method]:
```

Get a list of auto-generated methods.

#### See also

- [Method](method.md#method)
