"""
Day 13
List Comprehension
"""

print("=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# Squares

square = [i * i for i in range(1, 11)]

print("Squares")
print(square)

# Even Numbers

even = [i for i in range(1, 21) if i % 2 == 0]

print("\nEven Numbers")
print(even)

# Cubes

cube = [i ** 3 for i in range(1, 6)]

print("\nCubes")
print(cube)

# Names in Uppercase

names = ["ali", "sara", "ahmed"]

upper = [name.upper() for name in names]

print("\nUppercase Names")
print(upper)

print("=" * 50)