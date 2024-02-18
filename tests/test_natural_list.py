from promptu import NaturalList


class TestNaturalList:
    def test_str_returns_empty_string_when_items_is_empty(self):
        assert str(NaturalList([], "and")) == ""

    def test_str_returns_single_item_when_items_has_one_item(self):
        assert str(NaturalList(["foo"], "and")) == "foo"

    def test_str_returns_two_items_with_conjunction_when_items_has_two_items(self):
        assert str(NaturalList(["foo", "bar"], "and")) == "foo and bar"

    def test_str_returns_three_items_with_comma_and_conjunction_when_items_has_three_items(
        self,
    ):
        assert str(NaturalList(["foo", "bar", "baz"], "and")) == "foo, bar and baz"
