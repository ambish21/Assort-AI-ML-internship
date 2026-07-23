print("===== Simple Calculator =====")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operator = input("Enter operator (+, -, *, /): ")

match operator:

    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    case _:
        print("Invalid operator!")