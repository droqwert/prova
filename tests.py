# Unit tests for awsomeapp
from app import sum


def test_sum_calculation():
    # Given a :=5, b := 3
    # When it is called
    # Then it should return 8
    assert sum(5, 3) == 8, 'Calculate 5 + 3 '
