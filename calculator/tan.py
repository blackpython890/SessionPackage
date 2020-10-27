# tan.py

from math import tan, cos


__all__ = ['tan_']


def tan_(x : int) -> float:
    '''
    returns the tangent of x
    Input  : x
    Output : tan(x) measured in radians
    '''
    return f'The tangent of {x} is {tan(x)}'


def tan_derivative(x : int) -> float:
    '''
    returns the derivative of sin x
    Input : x
    Output : sec(x)* sec(x) measured in radians
    '''
    a = ( 1/ cos(x) )**2
    return f'The derivative of tangent {x} is {a}'