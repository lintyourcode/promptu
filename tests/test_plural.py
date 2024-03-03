import pytest

from promptu import pluralize


def test_pluralize_selects_first_option_when_items_has_one_item():
    assert pluralize("foo", "bar", ["baz"]) == "foo"


@pytest.mark.parametrize(
    "items",
    [[], ["foo", "bar"], ["foo", "bar", "baz"]],
)
def test_pluralize_selects_second_option_when_items_does_not_have_one_item(items):
    assert pluralize("foo", "bar", items) == "bar"
