from promptu import join


def test_join_returns_empty_string_when_items_is_empty():
    assert join([], "and") == ""


def test_join_returns_single_item_when_items_has_one_item():
    assert join(["foo"], "and") == "foo"


def test_join_returns_two_items_with_conjunction_when_items_has_two_items():
    assert join(["foo", "bar"], "and") == "foo and bar"


def test_join_returns_three_items_with_comma_and_conjunction_when_items_has_three_items():
    assert join(["foo", "bar", "baz"], "and") == "foo, bar and baz"
