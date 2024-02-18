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
```

## Prompting Utilities

### `NaturalList`

Formats a list of items as a natural language list.

**Syntax:**

```py
NaturalList(items: List, conjunction: str)
```
