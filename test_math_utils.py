import pytest
from math_utils import add, subtract, multiply, divide # Assuming functions are in math_utils.py


# Test cases for add function
def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_negative_integers():
    assert add(-2, -3) == -5

def test_add_mixed_integers():
    assert add(5, -3) == 2
    assert add(-5, 3) == -2

def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_float_numbers():
    assert add(2.5, 3.5) == 6.0
    assert add(1.1, 2.2) == pytest.approx(3.3)

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_negative_floats():
    assert add(-1.5, -2.5) == -4.0


# Test cases for subtract function
def test_subtract_positive_integers():
    assert subtract(5, 2) == 3

def test_subtract_negative_integers():
    assert subtract(-5, -2) == -3
    assert subtract(-2, -5) == 3

def test_subtract_mixed_integers():
    assert subtract(5, -2) == 7
    assert subtract(-5, 2) == -7

def test_subtract_with_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0

def test_subtract_float_numbers():
    assert subtract(5.5, 2.0) == 3.5
    assert subtract(3.3, 1.1) == pytest.approx(2.2)

def test_subtract_result_zero():
    assert subtract(5, 5) == 0

def test_subtract_negative_floats():
    assert subtract(-1.5, -2.5) == 1.0


# Test cases for multiply function
def test_multiply_positive_integers():
    assert multiply(2, 3) == 6

def test_multiply_negative_integers():
    assert multiply(-2, -3) == 6

def test_multiply_mixed_integers():
    assert multiply(2, -3) == -6
    assert multiply(-2, 3) == -6

def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0

def test_multiply_float_numbers():
    assert multiply(2.5, 2.0) == 5.0
    assert multiply(1.5, 0.5) == pytest.approx(0.75)

def test_multiply_by_one():
    assert multiply(5, 1) == 5
    assert multiply(-5, 1) == -5

def test_multiply_negative_floats():
    assert multiply(-1.5, 2.0) == -3.0


# Test cases for divide function
def test_divide_positive_numbers():
    assert divide(6, 3) == 2.0  # Division always returns float in Python 3
    assert divide(7, 2) == 3.5

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2.0
    assert divide(6, -3) == -2.0
    assert divide(-6, 3) == -2.0

def test_divide_by_one():
    assert divide(5, 1) == 5.0
    assert divide(-5, 1) == -5.0

def test_divide_zero_by_number():
    assert divide(0, 5) == 0.0
    assert divide(0, -5) == 0.0

def test_divide_float_numbers():
    assert divide(7.5, 2.5) == 3.0
    assert divide(10.0, 3.0) == pytest.approx(3.3333333333333335)

def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(-5, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(0, 0)
