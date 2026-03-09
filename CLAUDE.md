## Project Rules

- Every response must end with: `git commit -m "brief_summary_in_english"`

## Architecture

The call chain is linear:
**`app.py`** → **`carta_natal.py`** → **`chart_draw.py`**

## Python 3.12 Type Hint Rules (PEP 695 & 585)

- Use `type` statement for type aliases: `type MyList = list[int]`
- Use built-in generics: `list[]`, `dict[]`, `tuple[]`, `set[]`.
- Use `X | Y` for unions/optionals.
- Use PEP 695 generic syntax: `def fn[T](x: T)`, `class Stack[T]`.
- No `from __future__ import annotations`.
- Imports: Keep `TypedDict`, `Protocol`, `Callable`, `Literal`.
- Remove: `List`, `Dict`, `Tuple`, `Union`, `Optional`, `TypeVar` from `typing`.