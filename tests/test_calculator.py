''' Tests '''
import pytest
from calculator import Calculator

class TestCalculator:
    ''' CLass for Testing the Calculator Functions '''

    def setup_method(self):
        ''' Resets history before each test '''
        Calculator.clear_history()

    def test_add(self):
        ''' Tests for addition '''
        calc = Calculator()
        assert calc.add(1, 2) == 3

    def test_subtract(self):
        ''' Tests for subtraction '''
        calc = Calculator()
        assert calc.subtract(5, 3) == 2

    def test_multiply(self):
        ''' Tests for multiplication '''
        calc = Calculator()
        assert calc.multiply(2, 3) == 6

    def test_divide(self):
        ''' Tests for regular division '''
        calc = Calculator()
        assert calc.divide(6, 3) == 2

    def test_divide_by_zero(self):
        ''' Tests to catch divide by zero exception '''
        calc = Calculator()
        with pytest.raises(ZeroDivisionError):
            calc.divide(6, 0)

    def test_history(self):
        ''' Tests to check if history is accessible '''
        calc = Calculator()
        calc.add(1, 1)
        calc.subtract(2, 1)
        history = calc.get_history()
        assert len(history) == 2
        assert "Add" in history[0]
        assert "Subtract" in history[1]

    def test_clear_history(self):
        ''' Tests to check if clearing history works '''
        calc = Calculator()
        calc.add(1, 1)
        calc.clear_history()
        assert len(calc.get_history()) == 0
