"""
Day 13
reduce() Function
"""

from functools import reduce

print("=" * 50)
print("REDUCE FUNCTION")
print("=" * 50)

numbers = [10, 20, 30, 40]

print("Numbers")
print(numbers)

# Sum

total = reduce(lambda x, y: x + y, numbers)

print("\nTotal")
print(total)

# Product

product = reduce(lambda x, y: x * y, numbers)

print("\nProduct")
print(product)

print("=" * 50)