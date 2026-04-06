import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_data, expected_result", [
    ("     skypro", "skypro"),
    ("hello", "hello"),
    (" whitespace ", "whitespace"),
    ("", "")
])
def test_trim_positive(self, units, input_data, expected_result):
    assert string_utils.trim(input_data) == expected_result


@pytest.mark.negative
@pytest.mark.parametrize("invalid_input", [
    (258),
    (True),
    (["whitespace"]),
])
def test_trim_negative_types(self, units, input_data, expected_result):

    assert string_utils.trim(input_data) == expected_result


@pytest.mark.positive
@pytest.mark.parametrize("inrut_str, symbol, bool", [
    ("", "a", False),
    ("text", "", False),
    (None, "a", False)
])
def test_contains_negative(input_str, symbol, bool):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, symbol) == bool


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    utils = StringUtils()
    assert utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "v", "SkyPro")
])
def test_delete_symbol_negative(input_str, symbol, expected) -> None:
    utils = StringUtils
    assert utils.delete_symbol(input_str, symbol) == expected
