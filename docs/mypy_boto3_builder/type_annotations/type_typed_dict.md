# TypeTypedDict

> Auto-generated documentation for [mypy_boto3_builder.type_annotations.type_typed_dict](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py) module.

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

- [mypy-boto3-builder](../../README.md#mypy_boto3_builder) / [Modules](../../MODULES.md#mypy-boto3-builder-modules) / [Mypy Boto3 Builder](../index.md#mypy-boto3-builder) / [Type Annotations](index.md#type-annotations) / TypeTypedDict
    - [TypeTypedDict](#typetypeddict)
        - [TypeTypedDict().add_attribute](#typetypeddictadd_attribute)
        - [TypeTypedDict().copy](#typetypeddictcopy)
        - [TypeTypedDict().get_attribute](#typetypeddictget_attribute)
        - [TypeTypedDict().get_children_literals](#typetypeddictget_children_literals)
        - [TypeTypedDict().get_children_typed_dicts](#typetypeddictget_children_typed_dicts)
        - [TypeTypedDict().get_children_types](#typetypeddictget_children_types)
        - [TypeTypedDict().get_import_record](#typetypeddictget_import_record)
        - [TypeTypedDict().get_local_types](#typetypeddictget_local_types)
        - [TypeTypedDict().get_optional](#typetypeddictget_optional)
        - [TypeTypedDict().get_required](#typetypeddictget_required)
        - [TypeTypedDict().get_sort_key](#typetypeddictget_sort_key)
        - [TypeTypedDict.get_typing_import_record](#typetypeddictget_typing_import_record)
        - [TypeTypedDict().has_both](#typetypeddicthas_both)
        - [TypeTypedDict().has_optional](#typetypeddicthas_optional)
        - [TypeTypedDict().has_required](#typetypeddicthas_required)
        - [TypeTypedDict().is_dict](#typetypeddictis_dict)
        - [TypeTypedDict().is_same](#typetypeddictis_same)
        - [TypeTypedDict().is_stringified](#typetypeddictis_stringified)
        - [TypeTypedDict().is_typed_dict](#typetypeddictis_typed_dict)
        - [TypeTypedDict().iterate_children](#typetypeddictiterate_children)
        - [TypeTypedDict().render](#typetypeddictrender)
        - [TypeTypedDict().replace_self_references](#typetypeddictreplace_self_references)
        - [TypeTypedDict().requires_safe_render](#typetypeddictrequires_safe_render)
        - [TypeTypedDict().stringify](#typetypeddictstringify)
        - [TypeTypedDict().type_hint_annotations](#typetypeddicttype_hint_annotations)
    - [TypedDictAttribute](#typeddictattribute)
        - [TypedDictAttribute().get_type_annotation](#typeddictattributeget_type_annotation)
        - [TypedDictAttribute().is_required](#typeddictattributeis_required)
        - [TypedDictAttribute().iterate_types](#typeddictattributeiterate_types)
        - [TypedDictAttribute().render](#typeddictattributerender)

## TypeTypedDict

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L63)

```python
class TypeTypedDict(FakeAnnotation):
    def __init__(
        name: str,
        children: Iterable[TypedDictAttribute] = (),
        docstring: str = '',
        stringify: bool = False,
        replace_with_dict: Iterable[str] = tuple(),
    ) -> None:
```

Wrapper for `typing/typing_extensions.TypedDict` type annotations.

#### Arguments

- `name` - Type name.
- `children` - Typed dict attributes.
- `docstring` - Docstring for render.
- `stringify` - Convert type annotation to string to avoid circular deps.
- `replace_with_dict` - Render Dict[str, Any] instead to avoid circular dependencies.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)
- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().add_attribute

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L166)

```python
def add_attribute(
    name: str,
    type_annotation: FakeAnnotation,
    required: bool,
) -> None:
```

Add new attribute to a dictionary.

#### Arguments

- `name` - Argument name.
- `type_annotation` - Argument type annotation.
- `required` - Whether argument has to be set.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeTypedDict().copy

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L233)

```python
def copy() -> 'TypeTypedDict':
```

Create a copy of type annotation wrapper.

### TypeTypedDict().get_attribute

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L112)

```python
def get_attribute(name: str) -> TypedDictAttribute:
```

Find attribute by `name`.

#### Arguments

- `name` - Attribute name.

#### Returns

Found attribute.

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_children_literals

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L275)

```python
def get_children_literals(
    processed: Iterable['TypeTypedDict'] = tuple(),
) -> set[TypeLiteral]:
```

Extract required TypeLiteral list from attributes.

#### See also

- [TypeLiteral](type_literal.md#typeliteral)

### TypeTypedDict().get_children_typed_dicts

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L262)

```python
def get_children_typed_dicts() -> set['TypeTypedDict']:
```

Extract required TypeTypedDict list from attributes.

### TypeTypedDict().get_children_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L253)

```python
def get_children_types() -> set[FakeAnnotation]:
```

Extract required type annotations from attributes.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeTypedDict().get_import_record

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L160)

```python
def get_import_record() -> ImportRecord:
```

Get import record required for using type annotation.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeTypedDict().get_local_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L324)

```python
def get_local_types() -> list[FakeAnnotation]:
```

Get internal types generated by builder.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypeTypedDict().get_optional

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L223)

```python
def get_optional() -> list[TypedDictAttribute]:
```

Get a list of optional attributes.

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_required

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L213)

```python
def get_required() -> list[TypedDictAttribute]:
```

Get a list of required attributes.

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().get_sort_key

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L101)

```python
def get_sort_key() -> str:
```

Sort Typed Dicts by name.

### TypeTypedDict.get_typing_import_record

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L146)

```python
@staticmethod
def get_typing_import_record() -> ImportRecord:
```

Get import record required for using TypedDict.

Fallback to typing_extensions for py38-.

#### See also

- [ImportRecord](../import_helpers/import_record.md#importrecord)

### TypeTypedDict().has_both

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L207)

```python
def has_both() -> bool:
```

Whether TypedDict has both optional and required keys.

### TypeTypedDict().has_optional

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L189)

```python
def has_optional() -> bool:
```

Whether TypedDict has optional keys.

### TypeTypedDict().has_required

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L198)

```python
def has_required() -> bool:
```

Whether TypedDict has required keys.

### TypeTypedDict().is_dict

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L177)

```python
def is_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().is_same

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L245)

```python
def is_same(other: 'TypeTypedDict') -> bool:
```

Check whether typed dict attributes are the same as `other`.

### TypeTypedDict().is_stringified

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L89)

```python
def is_stringified() -> bool:
```

Whether TypedDict usage should be rendered as a string.

### TypeTypedDict().is_typed_dict

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L183)

```python
def is_typed_dict() -> bool:
```

Always True as it is a TypedDict.

### TypeTypedDict().iterate_children

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L315)

```python
def iterate_children() -> Iterator[TypedDictAttribute]:
```

Iterate over children from required to optional.

#### See also

- [TypedDictAttribute](#typeddictattribute)

### TypeTypedDict().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L128)

```python
def render(parent_name: str = '') -> str:
```

Render type annotation to a valid Python code for local usage.

#### Returns

A string with a valid type annotation.

### TypeTypedDict().replace_self_references

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L292)

```python
def replace_self_references() -> None:
```

Replace self refenrences with `Dict[str, Any]` to avoid circular dependencies.

### TypeTypedDict().requires_safe_render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L307)

```python
@property
def requires_safe_render() -> bool:
```

Whether TypedDict has reserved words and has to be rendered safely.

### TypeTypedDict().stringify

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L95)

```python
def stringify() -> None:
```

Render TypedDict usage as a string.

### TypeTypedDict().type_hint_annotations

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L330)

```python
@property
def type_hint_annotations() -> list[FakeAnnotation]:
```

Type annotations list from arguments and return type with internal types.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

## TypedDictAttribute

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L16)

```python
class TypedDictAttribute():
    def __init__(
        name: str,
        type_annotation: FakeAnnotation,
        required: bool,
    ) -> None:
```

TypedDict attribute wrapper.

#### Arguments

- `name` - Attribute name.
- `type_annotation` - Attribute type annotation.
- `required` - Whether the attribute has to be set.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypedDictAttribute().get_type_annotation

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L31)

```python
def get_type_annotation() -> FakeAnnotation:
```

Get wrapped for non-required type annotation or raw type annotation.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypedDictAttribute().is_required

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L56)

```python
def is_required() -> bool:
```

Whether argument is required.

### TypedDictAttribute().iterate_types

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L49)

```python
def iterate_types() -> Iterator[FakeAnnotation]:
```

Itera over type annotations.

#### See also

- [FakeAnnotation](fake_annotation.md#fakeannotation)

### TypedDictAttribute().render

[[find in source code]](https://github.com/youtype/mypy_boto3_builder/blob/main/mypy_boto3_builder/type_annotations/type_typed_dict.py#L40)

```python
def render(parent_name: str = '') -> str:
```

Render attribute to use in class-based TypedDict definition.

#### Returns

A string with argument definition.
