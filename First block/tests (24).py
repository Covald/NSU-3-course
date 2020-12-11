import pytest
from First import func
from cmath import sqrt


def test_1():
    with pytest.raises(ValueError):
        func(0, 0, 0)


def test_2():
    assert func(0, 1, 2) == [-2]


def test_3():
    assert func(1, 0, 2) == [sqrt(-2), -sqrt(-2)]


def test_4():
    assert func(1, 0, 0) == [0]


def test_5():
    assert func(0, 1, 0) == [0]


def test_6():
    assert func(0, 1, 1) == [-1]
