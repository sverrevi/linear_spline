from search_helper import binary_search
import numpy as np

def interp(x, xp, yp):

    """Evaluates linear spline function at input value x from a dataset xp and yp

    Args:
        x (float/int): Value at which linear spline function is evaluated
        xp (list/np.array): A sorted list containing floats or ints
        yp (list/np.array): Corresponding datapoints to xp

    Returns:
        A float evaluating y value to corresponding x input    
    """
    
    if len(xp) == 0 or len(yp) == 0:
        raise ValueError("Input data xp and yp can not be empty")
    if len(xp) != len(yp):
        raise ValueError("Input data xp and yp must have same length")

    x_index = binary_search(x, xp)
    if x_index == 0 or x_index == len(xp)-1:
        return yp[x_index]
    x0, x1 = xp[x_index], xp[x_index+1]
    y0, y1 = yp[x_index], yp[x_index+1]
    a = (y1-y0)/(x1-x0)
    return a*(x-x0) + y0