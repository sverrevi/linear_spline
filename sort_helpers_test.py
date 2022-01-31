from numpy import array
from sort_helpers import is_sorted, binary_search

def test_is_sorted():
    xp_sorted = array([0, 1, 2, 100])
    xp_unsorted = array([1, 0, 4, 2, 5])
    xp_empty = array([])

    assert is_sorted(xp_sorted)
    assert not is_sorted(xp_unsorted)
    assert is_sorted(xp_empty)

def test_binary_search():
    x1 = 2
    xp1 = array([1, 4, 9, 16, 25])
    expected1 = 0
    computed1 = binary_search(x1, xp1)
    
    x2 = 5.5
    xp2 = array([1, 2])
    expected2 = 1
    computed2 = binary_search(x2, xp2)

    x3 = -1
    xp3 = array([4])
    expected3 = 0
    computed3 = binary_search(x3, xp3)

    x4 = 10
    xp4 = array([])
    expected4 = 0
    computed4 = binary_search(x4, xp4)

    assert expected1 == computed1
    assert expected2 == computed2
    assert expected3 == computed3
    assert expected4 == computed4