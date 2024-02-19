import pytest

from promptu import plural


def test_plural_does_not_include_plural_only_string_when_items_has_one_item():
    assert plural("item(s)", ["foo"]) == "item"


@pytest.mark.parametrize(
    "items",
    [[], ["foo", "bar"], ["foo", "bar", "baz"]],
)
def test_plural_include_plural_only_string_when_items_does_not_have_one_item(items):
    assert plural("item(s)", items) == "items"


def test_plural_selects_first_option_when_items_has_one_item():
    assert plural("(foo|bar)", ["baz"]) == "foo"


@pytest.mark.parametrize(
    "items",
    [[], ["foo", "bar"], ["foo", "bar", "baz"]],
)
def test_plural_selects_second_option_when_items_does_not_have_one_item(items):
    assert plural("(foo|bar)", items) == "bar"


def test_plural_supports_multiple_patterns():
    assert plural("(foo)(bar|baz)", []) == "foobaz"