import os, sys # Flake8 error: multiple imports on one line (E401) and unused imports (F401)

# Black error: improper spacing and missing blank lines
def BadlyNamedFunction( x,y ):
    unused_var = 10 # Flake8 error: assigned to but never used (F841)
    return x+y 

# Mypy error: incompatible types (adding string to int) and missing return type
def type_error_example(a: int):
    return a + "this is a string"

# Pytest error: this assertion will always fail
def test_will_fail():
    assert 1 == 2, "This test is designed to break the pipeline"
