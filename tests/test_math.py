import pytest

def add_two_numbers(a, b):
    return a + b

@pytest.mark.math # This is pytest mark to execute marks
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "The sum of 1 and 2 should be 3"
    print("The sum of 1 and 2 should be 3")

@pytest.mark.math # This is pytest mark to execute marks
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400"
    print ("The sum of 100 and 300 should be 400")