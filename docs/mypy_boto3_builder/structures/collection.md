# Collection

> Auto-generated documentation for [mypy_boto3_builder.structures.collection](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py) module.

Boto3 ServiceResource or Resource collection.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Structures](index.md#structures) / Collection
    - [Collection](#collection)
        - [Collection().boto3_doc_link](#collectionboto3_doc_link)
        - [Collection().iterate_types](#collectioniterate_types)

## Collection

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L13)

```python
class Collection(ClassRecord):
    def __init__(
        name: str,
        attribute_name: str,
        parent_name: str,
        service_name: ServiceName,
        type_annotation: FakeAnnotation,
        object_class_name: str,
    ):
```

Boto3 ServiceResource or Resource collection.

#### See also

- [ClassRecord](class_record.md#classrecord)
- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
- [ServiceName](../service_name.md#servicename)

### Collection().boto3_doc_link

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L43)

```python
@property
def boto3_doc_link() -> str:
```

Link to boto3 docs.

### Collection().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/structures/collection.py#L50)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Iterate over all type annotations.

#### See also

- [FakeAnnotation](../type_annotations/fake_annotation.md#fakeannotation)
