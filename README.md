# Promptu

> Prompt engineering library for Python

## Example

```py
from promptu import NaturalList

class FindMatchingColor:
    def __init__(self, existing_colors):
        self.existing_colors = []

    def __str__(self):
        return f'What color goes well with {
            NaturalList(items=self.existing_colors, conjunction='and')
        }?'

# Prints "What color goes well with blue, purple and white?"
print(FindMatchingColor(['blue', 'purple', 'white']))
```

## Prompting Utilities

### `NaturalList`

Formats a list of items as a natural language list.

**Syntax:**

```py
NaturalList(items: List, conjunction: str)
```

### `plural()`

Selects the singular or plural form of a word based on the number of items.

**Syntax:**

```py
plural(template: str, items: List)
```

**Template rules:**

- `(str1|str2)` evaluates to `str1` if the number of items is 1, otherwise
  `str2`.
- `(str)` evaluates to `str` if the number of items is not 1.
