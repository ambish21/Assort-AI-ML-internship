from utils import calculator
from utils import string_utils
from utils import date_utils


def calculator_menu():

    while True:

        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")


        choice = input("Enter choice: ")


        match choice:

            case "1":
                a = float(input("First number: "))
                b = float(input("Second number: "))

                print(calculator.add(a,b))


            case "2":
                a = float(input("First number: "))
                b = float(input("Second number: "))

                print(calculator.subtract(a,b))


            case "3":
                a = float(input("First number: "))
                b = float(input("Second number: "))

                print(calculator.multiply(a,b))


            case "4":

                a = float(input("First number: "))
                b = float(input("Second number: "))

                print(calculator.divide(a,b))


            case "5":
                print("Exit...")
                break


            case _:
                print("Invalid choice")


calculator_menu()