"""
Day 13
map() Function
"""

print("=" * 50)
print("MAP FUNCTION")
print("=" * 50)

numbers = [10, 20, 30, 40, 50]

print("Original List")
print(numbers)

# Square

square = list(map(lambda x: x * x, numbers))

print("\nSquare")
print(square)

# Double

double = list(map(lambda x: x * 2, numbers))

print("\nDouble")
print(double)

# Convert to String

string_numbers = list(map(str, numbers))

print("\nString List")
print(string_numbers)

print("=" * 50)