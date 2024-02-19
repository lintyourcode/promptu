from typing import Any, List


def _prefix_item(items: Any, index: int, conjunction: str) -> str:
    item = items[index]
    if index == 0:
        return f"{item}"
    if index == len(items) - 1:
        return f" {conjunction} {item}"
    return f", {item}"


def natural_list(items: List, conjunction: str) -> str:
    """Format a list of items as a natural language list.

    :param items: The items to format.
    :param conjunction: The conjunction to use before the last item. For
        example, "and" or "or".
    """

    return "".join(
        _prefix_item(items, index, conjunction) for index in range(len(items))
    )
