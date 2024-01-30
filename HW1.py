def classify_triangle(a, b, c):
    # Sort the sides to simplify the logic
    sides = sorted([a, b, c])

    # Validation of triangle inequality theorem
    if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
        return "Not a valid triangle"

    # Check for right triangle
    is_right = (round(sides[0]**2, 6) + round(sides[1]**2, 6) == round(sides[2]**2, 6))
    # Classification based on side lengths
    if sides[0] == sides[2]:
        return "Equilateral Triangle" + (" and Right Triangle" if is_right else "")
    elif sides[0] == sides[1]:
        return "Isosceles Triangle" + (" and Right Triangle" if is_right else "")
    else:
        return "Scalene Triangle" + (" and Right Triangle" if is_right else "")

# Example usage
# classify_triangle(4, 4, 4 * (2 ** 0.5))  # Isosceles Right Triangle
