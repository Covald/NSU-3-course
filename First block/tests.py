from First import *
from cmath import sqrt
import unittest as ts


def test_one():
    ts.TestCase.assertRaises(ValueError, func(0, 0, 0))


def test_two():
    assert func(0, 1, 2) == [-2]


def test_3():
    assert func(1, 0, 2) == [sqrt(-2), -sqrt(-2)]


def test_4():
    assert func(1, 0, 0) == [0]


def test_5():
    assert func(0, 1, 0) == [0]


def test_6():
    assert func(0, 1, 1) == [-1]
