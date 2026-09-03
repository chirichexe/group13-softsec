import re

ALLOWED_ARITHMETIC_REGEX = re.compile(r"^[\d\s+\-*/().]+$")

def calculator(expr: str) -> str:
    """Evaluate an expression and return the result."""
    if not isinstance(expr, str):
        raise ValueError("Input must be a string")

    clean_expr = expr.strip()
    if not clean_expr:
        raise ValueError("Input cannot be empty")

    if not ALLOWED_ARITHMETIC_REGEX.fullmatch(clean_expr):
        raise ValueError("Invalid input")

    try:
        result = eval(clean_expr)
        return str(result)
    except Exception as e:
        raise ValueError(f"Invalid expression")
