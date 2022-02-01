from numpy import array
from sort_helper import binary_search

def test_binary_search():
    """Ensuring binary_search works as intended
        
        The following cases are tested:
            - x is between two xp datapoints
            - x is the same as one xp datapoint
            - x is outside xp datapoints on left bound
            - x is outside xp datapoints on right bound
            - xp is an empty array
    """

    x1 = 2
    xp1 = array([1, 4, 9, 16, 25])
    expected1 = 0
    computed1 = binary_search(x1, xp1)

    x2 = 4
    xp2 = array([1, 4, 9, 16, 25])
    expected2 = 1
    computed2 = binary_search(x2, xp2)
    
    x3 = 5.5
    xp3 = array([1, 2])
    expected3 = 1
    computed3 = binary_search(x3, xp3)

    x4 = -1
    xp4 = array([4])
    expected4 = 0
    computed4 = binary_search(x4, xp4)

    x5 = 10
    xp5 = array([])
    expected5 = 0
    computed5 = binary_search(x5, xp5)

    

    assert expected1 == computed1
    assert expected2 == computed2
    assert expected3 == computed3
    assert expected4 == computed4
    assert expected5 == computed5