from utils import calculator
from utils import string_utils
from utils import date_utils



def main():

    print("===== Calculator =====")

    print(
        calculator.add(10,5)
    )

    print(
        calculator.divide(10,2)
    )


    print("\n===== String Utility =====")


    text = "Python"

    print(
        string_utils.uppercase(text)
    )

    print(
        string_utils.reverse(text)
    )


    print("\n===== Date Utility =====")


    print(
        date_utils.current_date()
    )

    print(
        date_utils.current_time()
    )



main()