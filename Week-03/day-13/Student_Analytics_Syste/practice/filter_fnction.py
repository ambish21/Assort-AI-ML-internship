"""
Day 13
filter() Function
"""

print("=" * 50)
print("FILTER FUNCTION")
print("=" * 50)

numbers = [15, 20, 33, 40, 55, 60, 75]

print("Original List")
print(numbers)

# Even Numbers

even = list(filter(lambda x: x % 2 == 0, numbers))

print("\nEven Numbers")
print(even)

# Greater than 40

greater = list(filter(lambda x: x > 40, numbers))

print("\nGreater than 40")
print(greater)

print("=" * 50)