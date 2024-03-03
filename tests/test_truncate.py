import pytest

from promptu import TruncateMode, truncate


def test_truncate_by_character_returns_text_when_text_is_shorter_than_max_length():
    assert truncate("foo", 4) == "foo"


def test_truncate_by_character_returns_truncated_text_when_text_is_longer_than_max_length():
    assert truncate("foobar", 3) == "foo..."


def test_truncate_by_line_returns_text_when_text_has_fewer_lines_than_max_length():
    assert truncate("foo\nbar", 3, mode=TruncateMode.LINE) == "foo\nbar"


def test_truncate_by_line_returns_truncated_text_when_text_has_more_lines_than_max_length():
    assert truncate("foo\nbar\nbaz", 2, mode=TruncateMode.LINE) == "foo\nbar\n\n..."


def test_truncate_raises_value_error_when_mode_is_invalid():
    with pytest.raises(ValueError):
        truncate("foo", 3, mode="invalid")
