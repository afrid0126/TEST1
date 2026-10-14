import os, sys, time # Flake8: multiple imports on one line (E401) and unused imports (F401)
from math import * # Flake8: 'import *' is bad practice (F403)

# 1. FORMATTING & NAMING ERRORS (Caught by Black and Flake8)
def CALCULATE_stuff ( x,y ):
  a=x+y
  b =  x-y
  unused_variable = 99 # Flake8: Assigned but never used (F841)
  return a*b

# 2. TYPE CHECKING ERRORS (Caught by Mypy)
def process_payment(amount: float, card_number: str) -> bool:
    print(f"Processing card {card_number}")
    if amount < 0:
        return "Payment failed" # Mypy: Returning a string when the hint says 'bool'

    return True

user_id: int = "user_789" # Mypy: Assigning a string to an integer variable

# 3. LINTING & UNDEFINED ERRORS (Caught by Flake8)
def fetch_data():
    print(undefined_api_url) # Flake8: Undefined name (F821)
    
    # Black & Flake8: Line too long (E501)
    long_string = "This string is intentionally made very very very very very very very very very very very very long to trigger line length limit errors in linters."
    return None

# 4. UNIT TEST FAILURES (Caught by Pytest)
def test_calculate_stuff():
    result = CALCULATE_stuff(5, 5)
    # Pytest: This assertion will fail because (5+5) * (5-5) = 0, not 100
    assert result == 100, f"Expected 100, but got {result}" 

def test_process_payment():
    # Pytest: This will fail because process_payment returns "Payment failed" for negative numbers
    assert process_payment(-50.0, "1234") == True, "Negative payments should not pass"
