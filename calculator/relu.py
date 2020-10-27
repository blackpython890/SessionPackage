# relu.py


__all__ = ['relu_']


def relu_(x : float) -> float:
    '''
    The ReLU function returns 0 if it receives any negative input, but for any positive value x it returns that value back.
    Input  : x
    Output : return positive number
    '''
    if x < 0:
        raise ValueError('ReLU returns only positive number')
    else:
        return f'The ReLU activation function on {x} is {x}'


def relu_derivative(x : float) -> float:
    '''
    The function return the derivate of ReLU(x)
    Input  : x
    Output : ReLU(x)
    '''
    return f'The derivative of ReLU({x}) is 0'