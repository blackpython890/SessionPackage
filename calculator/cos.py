# cos.py

from math import sin, cos

__all__ = ['cos_']


def cos_(x : float) -> float:
    '''
    returns the cosine of x
    Input  : x
    Output : math.cos(x) measured in radians.
    '''
    return f'The cosine({x}) is {cos(x)}'


def cos_derivative(x : float) -> float:
    '''
    returns the derivative of cosine x
    Input : x
    Output : -math.sin(x) measured in radians.
    '''
    return f'The derivative of cosine({x}) is {-sin(x)}'