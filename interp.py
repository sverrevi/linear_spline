import matplotlib.pyplot as plt
from sort_helpers import is_sorted, binary_search


def interp(x, xp, yp):
    """Evaluates linear spline function at input value from a dataset xp and yp"""

    if not is_sorted(xp):
        raise ValueError("Input list xp must be sorted")
    x_index = binary_search(x, xp)
    if x_index == 0 or x_index == len(xp)-1:
        return yp[x_index]
    x0, x1 = xp[x_index], xp[x_index+1]
    y0, y1 = yp[x_index], yp[x_index+1]
    a = (y1-y0)/(x1- x0)
    return a*(x-x0) + y0
