"""Unit tests for calculator module."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add, subtract, multiply, divide, power, modulo, is_even, is_odd


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_add_mixed_numbers(self):
        assert add(-5, 3) == -2
        assert add(5, -3) == 2

    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_result_negative(self):
        assert subtract(3, 8) == -5

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(100, 0) == 0
        assert multiply(0, 100) == 0

    def test_multiply_by_one(self):
        assert multiply(100, 1) == 100
        assert multiply(1, 100) == 100

    def test_multiply_negative_numbers(self):
        assert multiply(-3, -3) == 9
        assert multiply(-3, 3) == -9

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_result_float(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_one(self):
        assert divide(100, 1) == 100

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_power_positive_exponent(self):
        assert power(2, 3) == 8
        assert power(3, 2) == 9

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1
        assert power(0, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25

    def test_power_one_exponent(self):
        assert power(100, 1) == 100

    def test_modulo_positive_numbers(self):
        assert modulo(10, 3) == 1
        assert modulo(15, 5) == 0

    def test_modulo_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot calculate modulo by zero"):
            modulo(10, 0)


class TestNumberHelpers:
    """Test cases for number helper functions."""

    def test_is_even_positive(self):
        assert is_even(2) is True
        assert is_even(4) is True
        assert is_even(100) is True

    def test_is_even_negative(self):
        assert is_even(-2) is True
        assert is_even(-4) is True

    def test_is_even_odd_numbers(self):
        assert is_even(1) is False
        assert is_even(3) is False
        assert is_even(99) is False

    def test_is_even_zero(self):
        assert is_even(0) is True

    def test_is_odd_positive(self):
        assert is_odd(1) is True
        assert is_odd(3) is True

    def test_is_odd_negative(self):
        assert is_odd(-1) is True
        assert is_odd(-3) is True

    def test_is_odd_even_numbers(self):
        assert is_odd(2) is False
        assert is_odd(4) is False
        assert is_odd(100) is False

    def test_is_odd_zero(self):
        assert is_odd(0) is False


class TestFailingDemo:
    """INTENTIONALLY FAILING TESTS - These simulate bugs in the application."""

    def test_add_returns_wrong_result(self):
        """BUG: add() returns wrong sum - expects 6 but should be 5."""
        assert add(2, 3) == 6

    def test_subtract_returns_wrong_result(self):
        """BUG: subtract() returns wrong difference - expects 7 but should be 6."""
        assert subtract(10, 4) == 7

    def test_multiply_returns_wrong_result(self):
        """BUG: multiply() returns wrong product - expects 15 but should be 12."""
        assert multiply(3, 4) == 15

    def test_divide_returns_wrong_result(self):
        """BUG: divide() returns wrong quotient - expects 3 but should be 2."""
        assert divide(10, 5) == 3

    def test_power_returns_wrong_result(self):
        """BUG: power() returns wrong value - expects 9 but should be 8."""
        assert power(2, 3) == 9

    def test_modulo_returns_wrong_result(self):
        """BUG: modulo() returns wrong remainder - expects 0 but should be 2."""
        assert modulo(7, 5) == 0
