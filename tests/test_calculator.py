'''My Calculator Tests'''
import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(6,2) == 8

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(5,2) == 3

def test_multiplication():
    '''Test that multiplication function works '''    
    assert multiply(8,8) == 64

def test_division():
    '''Test that division function works '''    
    assert divide(5,5) == 1.0

def test_division_by_zero():
    '''Test that divide by zero should not work '''    
    with pytest.raises(ValueError,match="Division by zero is not allowed"):
        assert divide(10,0)
