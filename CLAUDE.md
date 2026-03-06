# Reglas del proyecto

- Por cada cambio que hagas agrega al final una linea de: git commit -m "" explicando en una sola linea y en ingles un resumen de los cambios hechos.

## Python 3.12 Type Hint Rules

When formatting or refactoring Python files, enforce these rules:

- Use `type` statement for type aliases: `type MyList = list[int]`
- Use built-in generics — never `typing.List`, `typing.Dict`, `typing.Tuple`, `typing.Set`
- Use `X | Y` for unions — never `Union[X, Y]` or `Optional[X]` (use `X | None` instead)
- Use PEP 695 generic syntax for functions: `def fn[T](x: T) -> T`
- Use PEP 695 generic syntax for classes: `class Stack[T]:`
- Use PEP 695 `type` aliases with generics: `type Pair[T] = tuple[T, T]`
- Remove `from __future__ import annotations` — not needed in 3.12
- Remove obsolete `typing` imports: `List`, `Dict`, `Tuple`, `Set`, `FrozenSet`, `Type`, `Union`, `Optional`, `TypeVar` (when replaced by `[T]` syntax)
- Keep from `typing`: `TypedDict`, `Protocol`, `NamedTuple`, `Callable`, `ClassVar`, `Final`, `Literal`, `Annotated`, `overload`, `cast`, `TYPE_CHECKING`