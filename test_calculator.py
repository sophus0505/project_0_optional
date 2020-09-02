
import calculator
import pytest
from math import factorial, sin

@pytest.mark.parametrize(
    'arg, exp_out', [[(1, 2), 3], [(3, 4), 7], [(1, 0), 1]]
)
def test_add(arg, exp_out):
    assert calculator.add(arg[0], arg[1]) == exp_out

@pytest.mark.parametrize(
    'float, exp_out', [[(0.1, 0.2), 0.3], [(0.5, 0.7), 1.2], [(10.7, 3.5), 14.2]]
)
def test_add_float(float, exp_out):
    tol = 1e-7
    assert abs(calculator.add(float[0], float[1]) - exp_out) < tol

@pytest.mark.parametrize(
    'str, exp_out', [[('Hello', 'world'), 'Hello world'],
    [('flaske', 'hals'), 'flaske hals'], [('super', 'mann'), 'super mann']]
)
def test_add_str(str, exp_out):
    assert calculator.add(str[0], str[1]) == exp_out

@pytest.mark.parametrize(
    'n, exp_out', [[4, 24], [8, factorial(8)], [15, factorial(15)]]
)
def test_factorial(n, exp_out):
    assert calculator.factorial(n) == exp_out

@pytest.mark.parametrize(
    'arg, exp_out', [[(8, 50), sin(8)], [(26, 50), sin(26)], [(15, 50), sin(15)]]
)
def test_sin(arg, exp_out):
    tol = 1e-7
    assert abs(calculator.sin(arg[0], arg[1]) - exp_out) < tol

@pytest.mark.parametrize(
    'arg, exp_out', [[(6, 3), 2], [(30, 3), 10], [(1000, 4), 250]]
)
def test_divide(arg, exp_out):
    assert calculator.divide(arg[0], arg[1]) == exp_out

@pytest.mark.parametrize(
    'arg, exp_out', [[(5, 6), 30], [(6, 7), 42], [(56, 0), 0]]
)
def test_multiply(arg, exp_out):
    assert calculator.multiply(arg[0], arg[1]) == exp_out

@pytest.mark.parametrize(
    'arg, exp_out', [[(2, 6), 64], [(5, 2), 25], [(13, 3), 2197]]
)
def test_exponent(arg, exp_out):
    assert calculator.exponent(arg[0], arg[1]) == exp_out

@pytest.mark.parametrize(
    'args', [('Hello', 5), (67, 'Pencil'), ('Elephant', 86)]
)
def test_add__raises_TypeError_for_string_arguments(args):
    with pytest.raises(TypeError):
        calculator.add(args[0], args[1])

@pytest.mark.parametrize(
    'numerator, denomerator', [(5, 0), (0.5, 0), (76, 0), (-89, 0)]
)
def test_divide_raises_ZeroDivisionError_when_y_is_0(numerator, denomerator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(numerator, denomerator)
