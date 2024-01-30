def classify_triangle(a, b, c):
    # Check for invalid triangle
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "NotATriangle"

    # Check for types of triangles
    if a == b and b == c:
        return "Equilateral"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if a == b or b == c or a == c:
            return "Isosceles and Right"
        else:
            return "Scalene and Right" # Bug: Should be checked before Isosceles and Right
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example usage
print(classify_triangle(3, 4, 5)) # Should return 'Scalene and Right'
