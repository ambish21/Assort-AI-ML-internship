"""
Day 13
Lambda Functions
"""

print("=" * 50)
print("LAMBDA FUNCTION EXAMPLES")
print("=" * 50)

# Example 1
square = lambda x: x * x

print("Square of 5 :", square(5))

# Example 2
cube = lambda x: x ** 3

print("Cube of 4 :", cube(4))

# Example 3
addition = lambda a, b: a + b

print("Addition :", addition(20, 30))

# Example 4
maximum = lambda a, b: a if a > b else b

print("Maximum :", maximum(15, 40))

print("=" * 50)