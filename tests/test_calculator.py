import pytest
from cicd_intro.calculator_cli import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(2.5, 0.5) == 3.0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 1) == 2
    assert subtract(1, 0.5) == 0.5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0

def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 2) == 2.5
    assert divide(-1, 1) == -1

    # Test for division by zero using pytest.raises
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
