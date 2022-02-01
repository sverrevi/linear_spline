
def binary_search(x, xp, start_index=0):
    """Returns index of xp[i] so that xp[i]<= x <=x[i+1]
    
    Args:
        x (float/int): Value at which linear spline function is evaluated
        xp (list/np.array): A sorted list containing floats or ints
        yp (list/np.array): Corresponding datapoints to xp

    Returns:
        A float evaluating y value to corresponding x input    
    """
    if len(xp)<=1:
        return start_index
    midpoint = int(len(xp)/2)
    if x < xp[midpoint]:
        return binary_search(x, xp[:midpoint], start_index=start_index)
    else:
        start_index += midpoint
        return binary_search(x, xp[midpoint:], start_index=start_index)

