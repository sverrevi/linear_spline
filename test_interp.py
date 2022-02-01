from numpy import array, sin, linspace, pi
from interp import interp
import pytest


def test_interp():
    tol = 1e-5

    x1 = 3.5
    xp1 = array([1, 2, 3, 4, 5])
    yp1 = array([1, 7, 10, 13, 16])
    expected1 = 11.5
    computed1 = interp(x1, xp1, yp1)
    assert abs(expected1 - computed1) < tol

    x2 = 2.2
    xp2 = array([-10, 2.2, 55, 100, 120, 150])
    yp2 = array([1, 9, 14, 28, 500, 1000])
    expected2 = 9
    computed2 = interp(x2, xp2, yp2)
    assert abs(expected2 - computed2) < tol

    x3 = -50
    xp3 = array([-14, -1])
    yp3 = array([1, 50])
    expected3 = 1
    computed3 = interp(x3, xp3, yp3)
    assert abs(expected3 - computed3) < tol

    x4 = 20
    xp4 = array([1, 2, 3, 4, 5])
    yp4 = array([1, 3, 8, 13, 7801])
    expected4 = 7801
    computed4 = interp(x4, xp4, yp4)
    assert abs(expected4 - computed4) < tol

    x5 = 3
    xp5 = array([])
    yp5 = array([])
    with pytest.raises(ValueError) as excinfo:
        interp(x5, xp5, yp5)
    assert "Input data xp and yp can not be empty" in str(excinfo.value)

    x6 = 10
    xp6 = array([1, 2, 3])
    yp6 = array([1, 3])
    with pytest.raises(ValueError) as excinfo:
        interp(x6, xp6, yp6)
    assert "Input data xp and yp must have same length" in str(excinfo.value)

    x7 = 0.8*pi
    n = int(10e6)
    xp7 = linspace(0, 2*pi, n)
    yp7 = sin(xp7)
    expected7 = sin(x7)
    computed7 = interp(x7, xp7, yp7)
    assert abs(expected7 - computed7)