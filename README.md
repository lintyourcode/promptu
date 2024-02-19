# Promptu

> Prompt engineering library for Python

## Example

```py
from promptu import natural_list

def find_matching_color(existing_colors):
    return f'What color goes well with {natural_list(items=existing_colors, conjunction="and")}?'

# Prints "What color goes well with blue, purple and white?"
print(find_matching_color(['blue', 'purple', 'white']))
```

## Prompting Utilities

### `natural_list()`

Formats a list of items as a natural language list.

**Syntax:**

```py
natural_list(items: List, conjunction: str)
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
