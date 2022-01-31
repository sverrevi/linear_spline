
def is_sorted(xp):
    for i in range(len(xp)-1):
        if xp[i+1] < xp[i]:
            return False
    return True

def binary_search(x, xp, start_index=0):
    if len(xp)<=1:
        return start_index
    midpoint = int(len(xp)/2)
    if x < xp[midpoint]:
        return binary_search(x, xp[:midpoint], start_index=start_index)
    else:
        start_index += midpoint
        return binary_search(x, xp[midpoint:], start_index=start_index)

