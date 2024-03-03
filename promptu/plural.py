from typing import List


def plural(singular: str, plural: str, items: List) -> str:
    """
    Select the singular or plural form of a word based on the number of items.

    :param singular: Singular form of the word.
    :param plural: Plural form of the word.
    :param items: Items to count.
    """

    return singular if len(items) == 1 else plural
