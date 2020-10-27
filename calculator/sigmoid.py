# sigmoid.py


from math import exp


__all__ = ['sigmoid_']


def sigmoid_(x : float) ->  float:
    '''
    This function return the value of function S(x) = 1 / ( 1 + exp(-x) )
    Input  : x
    Output : S(x)
    '''
    a = 1 / ( 1 + exp(-x) )
    return f'The sigmoid or S({x}) is {a}'


def sigmoid_derivative(x : float) -> float:
    '''
    This function return the derivative of S(x) = 1 / ( 1 + exp(-x) ).
    Input  : x
    Output : S'(x)
    '''
    a = 1 / ( 1 + exp(-x) )
    b = a * ( 1 - a )
    return f'The derivative of Sigmoid({x}) or S({x}) is {b}'