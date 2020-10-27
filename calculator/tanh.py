# tan.py

from math import tanh


__all__ = ['tanh_']


def tanh_(x : float) -> float:
    '''
    return the hyperbloic tangent of x
    Input  : x
    Output : math.tanh(x)
    '''
    return f' The hyperbolic tangent of {x} is {tanh(x)}'


def tanh_derivative( x : float ) -> float:
    '''
    return the derivative of hyperbolic tangent of x
    Input  : x
    Output : 1 - ( tanh(x) )**2
    '''
    a = 1 - ( tanh(x) )**2
    return f'The derivative of hyperbolic tanh of {x} is {a}'