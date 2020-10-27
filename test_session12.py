import pytest, os
import calculator
from calculator import derivatives


#1
def test_package_set():
    assert calculator.__package__ == 'calculator'


#2
def test_calc_all():
    assert calculator.__all__ == [['cos_', 'exp_', 'log_', 'sin_', 'tan_', 'tanh_', 'relu_', 'sigmoid_']]


#3
def test_calc_name():
    assert calculator.__name__ == 'calculator'


#4
def test_calc_file():
    assert '__init__.py' in calculator.__file__


#5
def test_calc_path():
    assert type(calculator.__path__) == type([3,4])



#6
def test_calc_func():
    assert calculator.cos_(6)
    assert calculator.sin_(6)


#7
def test_calc_subpackage():
    assert 'sin_derivative' in dir(derivatives)


#8
def test_calc_not_import():
    assert 'sin_derivative' not in dir(calculator)
