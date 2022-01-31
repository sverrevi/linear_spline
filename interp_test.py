from numpy import array
from interp import interp

def test_interp():
    tol = 1e-5

    x1 = 3.5
    xp1 = array([1, 2, 3, 4, 5])
    yp1 = array([1, 7, 10, 13, 16])
    expected1 = 11.5
    computed1 = interp(x1, xp1, yp1)

    x2 = 1
    xp2 = array([1, 2, 3, 4, 5])
    yp2 = array([1, 7, 10, 13, 16])
    expected2 = 1
    computed2 = interp(x2, xp2, yp2)

    x3 = 0
    xp3 = array([1, 2, 3, 4, 5])
    yp3 = array([1, 7, 10, 13, 16])
    expected3 = 1
    computed3 = interp(x3, xp3, yp3)

    x4 = 20
    xp4 = array([1, 2, 3, 4, 5])
    yp4 = array([1, 7, 10, 13, 16])
    expected4 = 16
    computed4 = interp(x4, xp4, yp4)

    #TODO: Add more test cases
    #x5 = 3
    #xp5 = array([])
    #yp5 = array([])
 
    assert expected1 - computed1 < tol
    assert expected2 - computed2 < tol
    assert expected3 - computed3 < tol
    assert expected4 - computed4 < tol
