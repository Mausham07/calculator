"""
Name: Mausham Bista
"""

import calculator
from calculator import mb_add, mb_cos, mb_divide, mb_exponent, mb_multiply, mb_sin, mb_squareRoot, mb_sub, mb_tan
import pytest

def test_add():

    assert mb_add(2, 3) == 5

def test_sub():
    assert mb_sub(5, 2) == 3

def test_multiply():
    assert mb_multiply(2, 4) == 8

def test_division():
    assert mb_divide(10, 2) == 5

def test_squareRoot():
    assert mb_squareRoot(4) == 2
    
def test_exponent():
    assert mb_exponent(2, 3) == 8

def test_sin():
    assert mb_sin(0) == 0

def test_cos():
    assert mb_cos(0) == 1

def test_tan():
    assert mb_tan(0) == 0

pytest.main(["-v", "--tb=line", "-rN", __file__])