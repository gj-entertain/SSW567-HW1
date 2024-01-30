import pytest
from HW1 import classify_triangle

def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "NotATriangle"

def test_equilateral_triangle():
    assert classify_triangle(1, 1, 1) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"

def test_isosceles_right_triangle():
    assert classify_triangle(1, 1, 2**0.5) == "Isosceles and Right"
