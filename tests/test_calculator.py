import pytest
from calculator import calculator


# Verify simple arithmetic evaluation, operator precedence, and whitespace trimming
@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("1 + 1", "2"),
        ("2 * (3 + 4)", "14"),
        ("10 / 4", "2.5"),
        ("  5 - 2  ", "3"),
    ],
)
def test_calculator_evaluates_valid_expressions(expression, expected):
    assert calculator(expression) == expected


# Verify rejection of empty strings, non-whitelisted characters, 
# syntax errors and zero division.
@pytest.mark.parametrize(
    "expression",
    [
        "",
        "   ",
        "hello",
        "__import__('os').system('echo unsafe')",
        "1 / 0",
        "1 +",
    ],
)
def test_calculator_rejects_invalid_expressions(expression):
    with pytest.raises(ValueError):
        calculator(expression)


# Verify explicit type validation when input is not a string.
def test_calculator_rejects_non_string_input():
    with pytest.raises(ValueError, match="Input must be a string"):
        calculator(42)
