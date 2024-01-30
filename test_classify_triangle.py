import pytest
from HW1 import classify_triangle

def test_invalid_triangle():
    assert classify_triangle(0, 0, 0) == "Not a valid triangle"

def test_equilateral_triangle():
    assert classify_triangle(1, 1, 1) == "Equilateral Triangle"

def test_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles Triangle"

def test_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene Triangle"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene Triangle and Right Triangle"

def test_isosceles_right_triangle():
    assert classify_triangle(4, 4, 4*2**0.5) == "Isosceles Triangle and Right Triangle"

