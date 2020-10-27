# sin.py

from math import sin, cos


__all__ = ['sin_']


def sin_(x : int) -> float:
    '''
    returns the sine of x
    Input  : x
    Output : sin(x) measured in radians
    '''
    return f'The sin({x}) is {sin(x)}'



def sin_derivative(x : int) -> float:
    '''
    returns the derivative of sin x
    Input : x
    Output : cos(x) measured in radians
    '''
    return f'The derivative of sin({x}) is {cos(x)}'