# log.py

from math import log, e


__all__ = ['log_']


def log_( x : float, b : float = e ) -> float:
    '''
    returns the logarithm of x to the given base.
    Input  : x => positive number and b -> positive base.
    Output : math.log(x,b)
    '''
    if x < 0 or b < 0:
        raise ValueError('Invalid Inputs')
    else:
        return f'The logarithm of {x} to the given base {b} is {log(x, b)}'


def log_derivative( x : float, b : float = e ) -> float:
    '''
    returns the derivative of logarithm x to the given base.
    Input  : x => positive number and b -> positive base.
    Output : math.log(x,b)
    '''
    if x < 0 or b < 0:
        raise ValueError('Invalid Inputs')
    else:
        pass