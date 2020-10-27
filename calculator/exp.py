# exp.py

from math import exp


__all__ = ['exp_']


def exp_(x : float) -> float:
    '''
    return e raised to the power x
    Input  : x
    Output : math.exp(x)
    '''
    return f'e raised to the power {x} is {exp(x)}'


def exp_derivative(x : float) -> float:
    '''
    return the derivate of exponent of x
    Input  : x
    Output : math.exp(x)
    '''
    return f'The derivate of e raised to the power {x} is {exp(x)}'