def well_named_function(x: int, y: int) -> None:
    """A sample function."""
    print(f"Values are {x} and {y}")


def type_hint_success(a: int) -> int:
    """Adds 5 to the input."""
    return a + 5


def normal_blank_lines() -> None:
    """Demonstrates normal variable usage."""
    used_variable = 42
    short_line = f"This is fine now {used_variable}"
    print(short_line)


def test_always_passes() -> None:
    """A test that will pass pytest."""
    assert 2 == 2, "This assertion will pass"
