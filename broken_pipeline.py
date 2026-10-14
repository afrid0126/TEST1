def calculate_stuff(x: int, y: int) -> int:
    a = x + y
    b = x - y
    return a * b


def process_payment(amount: float, card_number: str) -> bool:
    print(f"Processing card {card_number}")
    if amount < 0:
        return False

    return True


user_id: str = "user_789"


def fetch_data() -> None:
    api_url = "https://api.example.com"
    print(api_url)

    short_string = "This string is short enough to pass line length limits."
    print(short_string)


def test_calculate_stuff() -> None:
    result = calculate_stuff(5, 5)
    assert result == 0, f"Expected 0, but got {result}"


def test_process_payment() -> None:
    assert process_payment(-50.0, "1234") is False, (
        "Negative payments should fail"
    )
