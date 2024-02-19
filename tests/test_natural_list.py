from promptu import natural_list


def test_str_returns_empty_string_when_items_is_empty():
    assert natural_list([], "and") == ""


def test_str_returns_single_item_when_items_has_one_item():
    assert natural_list(["foo"], "and") == "foo"


def test_str_returns_two_items_with_conjunction_when_items_has_two_items():
    assert natural_list(["foo", "bar"], "and") == "foo and bar"


def test_str_returns_three_items_with_comma_and_conjunction_when_items_has_three_items():
    assert natural_list(["foo", "bar", "baz"], "and") == "foo, bar and baz"
