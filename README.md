# Promptu

> Natural language generation utilities for prompt engineering

## Example

```py
from promptu import join

def find_matching_color(existing_colors):
    return f'What color goes well with {join(items=existing_colors, conjunction="and")}?'

# Prints "What color goes well with blue, purple and white?"
print(find_matching_color(['blue', 'purple', 'white']))
```

## Using in Langchain

```py
runnable = (
    {'prompt': RunnableLambda(find_matching_color)}
    | PromptTemplate.from_template('{prompt}')
    | model
)
runnable.invoke(['blue', 'purple', 'white'])
```

## Prompting Utilities

### `join()`

Formats a list of items as a natural language list.

**Syntax:**

```py
join(items: List, conjunction: str)
```

### `pluralize()`

Selects the singular or plural form of a word based on the number of items.

**Syntax:**

```py
pluralize(singular: str, plural: str, items: List)
```
