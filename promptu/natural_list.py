from typing import Any, List


class NaturalList:
    """Format a list of items as a natural language list."""

    def __init__(self, items: List, conjunction: str) -> None:
        """
        :param items: The items to format.
        :param conjunction: The conjunction to use before the last item. For
            example, "and" or "or".
        """

        self.items = items
        self.conjunction = conjunction

    def _prefix_item(self, item: Any, index: int) -> str:
        if index == 0:
            return f"{item}"
        if index == len(self.items) - 1:
            return f" {self.conjunction} {item}"
        return f", {item}"

    def __str__(self) -> str:
        return "".join(
            self._prefix_item(item, index) for index, item in enumerate(self.items)
        )
