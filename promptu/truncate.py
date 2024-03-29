from enum import Enum


class TruncateMode(Enum):
    CHARACTER = "character"
    LINE = "line"


def _truncate_by_character(text: str, max_length: int, suffix: str) -> str:
    if len(text) <= max_length:
        return text
    else:
        return f"{text[:max_length]}{suffix}"


def _truncate_by_line(text: str, max_length: int, suffix: str) -> str:
    lines = text.split("\n")
    if len(lines) <= max_length:
        return text
    else:
        truncated_text = "\n".join(lines[:max_length])
        return f"""{truncated_text}

{suffix}"""


def truncate(text: str, max_length: int, mode=None, suffix="...") -> str:
    """
    Truncate a string to a maximum length.

    If the text is longer than the maximum length, all characters or lines after
    the maximum length are replaced with the suffix.

    :param text: Text to truncate.
    :param max_length: Maximum length of the resulting text when `mode` is
        CHARACTER, or maximum number of lines when `mode` is LINE, not including
        the suffix.
    :param mode: Unit of `max_length`.
    :param suffix: Suffix to append if the text is truncated.

    :return: Truncated text.

    :raises ValueError: If `mode` is not a valid truncation mode.
    """

    if mode is None:
        mode = TruncateMode.CHARACTER
    if mode == TruncateMode.CHARACTER:
        return _truncate_by_character(text, max_length, suffix)
    elif mode == TruncateMode.LINE:
        return _truncate_by_line(text, max_length, suffix)
    else:
        raise ValueError("Invalid truncation mode")
