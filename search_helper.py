
def binary_search(x, xp, current_index=0):
    """Returns index of xp[i] such that xp[i]<= x <=x[i+1]
    
    Args:
        x (float/int): Value at which linear spline function is evaluated.
        xp (list/np.array): A sorted list containing floats or ints.
    
    Kwargs:
        current_index (int): Keyword argument used for recursive purposes. Should not be changed.

    Returns:
        Int corresponding to the index of last xp value less than x.
    """
    if len(xp)<=1:
        return current_index
    midpoint = int(len(xp)/2)
    if x < xp[midpoint]:
        return binary_search(x, xp[:midpoint], current_index=current_index)
    else:
        current_index += midpoint
        return binary_search(x, xp[midpoint:], current_index=current_index)