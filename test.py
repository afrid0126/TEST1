import os
import sys, math # Linter error: multiple imports on one line (E401)
import module_that_does_not_exist # Runtime/CI error: ModuleNotFoundError

# 1. SYNTAX & INDENTATION ERRORS (Fails compilation/execution immediately)
def badly_named_function( x,y ): # Linter error: bad spacing and naming
print("This will throw an IndentationError") 

if True # SyntaxError: missing colon
    print("This will also fail to parse")

# 2. TYPE CHECKING ERRORS (Fails Mypy)
def type_hint_failure(a: int) -> int:
    return a + "this is a string"

x: int = "hello"

# 3. LINTER & FORMATTING ERRORS (Fails Flake8, Black, Pylint)
def TooManyBlankLines():



    unused_variable = 42 # Linter error: unused variable
    line_too_long = "This string is unnecessarily long and will definitely trigger an E501 line too long warning in standard flake8 configurations which limit lines to 79 or 88 characters."
    return

# 4. RUNTIME EXCEPTIONS (Fails on execution)
division_by_zero = 10 / 0
print(undefined_variable)

# 5. TEST FAILURES (Fails Pytest / Unittest)
def test_always_fails():
    assert 1 == 2, "This assertion will always fail the test suite"

# 6. HARD EXIT (Guarantees pipeline failure if executed)
sys.exit(1)
