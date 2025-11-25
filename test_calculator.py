import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0, 5) == -5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 100) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-10, 2) == -5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

def test_power():
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 2) == 25
    assert calc.power(10, 0) == 1

def test_modulo():
    calc = Calculator()
    assert calc.modulo(10, 3) == 1
    assert calc.modulo(15, 4) == 3
    assert calc.modulo(20, 5) == 0
    assert calc.modulo(7, 2) == 1

def test_modulo_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot perform modulo by zero"):
        calc.modulo(10, 0)