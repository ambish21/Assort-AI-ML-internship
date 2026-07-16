# Simple Calculator

print("===== Simple Calculator =====")

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask user to choose an operation
print("\nChoose an operation")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Result =", result)

elif operator == "-":
    result = num1 - num2
    print("Result =", result)

elif operator == "*":
    result = num1 * num2
    print("Result =", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid operator!")