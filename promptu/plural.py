import re
from typing import List


def plural(template: str, items: List) -> str:
    """
    Select the singular or plural form of a word based on the number of items.

    :param template: Pattern used to construct the singular and plural forms.
    :param items: Items to count.

    Template syntax:
    - `(str1|str2)` evaluates to `str1` if the number of items is 1, otherwise
        `str2`.
    """

    return re.sub(
        r"\(([^)|]+)\|([^)]+)\)", r"\1" if len(items) == 1 else r"\2", template
    )
