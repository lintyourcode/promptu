import re
from typing import List


class Plural:
    """
    Select the singular or plural form of a word based on the number of items.
    """

    def __init__(self, template: str, items: List):
        """
        :param template: Pattern used to construct the singular and plural
            forms.
        :param items: Items to count.

        Template rules:
        - `(str1|str2)` evaluates to `str1` if the number of items is 1,
            otherwise `str2`.
        - `(str)` evaluates to `str` if the number of items is not 1.
        """

        self.template = template
        self.items = items

    def __str__(self) -> str:
        is_singular = len(self.items) == 1
        word = re.sub(
            r"\(([^)|]+)\|([^)]+)\)", r"\1" if is_singular else r"\2", self.template
        )
        return re.sub(r"\(([^)]+)\)", "" if is_singular else r"\1", word)
