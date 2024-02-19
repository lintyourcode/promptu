import pytest

from promptu import Plural


class TestPlural:
    def test_str_does_not_include_plural_only_string_when_items_has_one_item(self):
        assert str(Plural("item(s)", ["foo"])) == "item"

    @pytest.mark.parametrize(
        "items",
        [[], ["foo", "bar"], ["foo", "bar", "baz"]],
    )
    def test_str_include_plural_only_string_when_items_does_not_have_one_item(
        self, items
    ):
        assert str(Plural("item(s)", items)) == "items"

    def test_str_selects_first_option_when_items_has_one_item(self):
        assert str(Plural("(foo|bar)", ["baz"])) == "foo"

    @pytest.mark.parametrize(
        "items",
        [[], ["foo", "bar"], ["foo", "bar", "baz"]],
    )
    def test_str_selects_second_option_when_items_does_not_have_one_item(self, items):
        assert str(Plural("(foo|bar)", items)) == "bar"

    def test_str_supports_multiple_patterns(self):
        assert str(Plural("(foo)(bar|baz)", [])) == "foobaz"
