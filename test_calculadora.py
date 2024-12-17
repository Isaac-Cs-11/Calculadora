import pytest
from calculadora import suma, resta, multiplicacion, division

def test_suma():
    assert suma(3, 5) == 8
    assert suma(-2, -3) == -5

def test_resta():
    assert resta(10, 5) == 5
    assert resta(-2, -3) == 1

def test_multiplicacion():
    assert multiplicacion(3, 5) == 15
    assert multiplicacion(-2, 3) == -6

def test_division():
    assert division(10, 2) == 5
    assert division(-6, 3) == -2
    with pytest.raises(ValueError):
        division(5, 0)
