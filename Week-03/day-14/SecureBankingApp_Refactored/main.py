# main.py

from bank import Bank
from logger_config import logger


def menu():
    print("\n" + "=" * 40)
    print("      SECURE BANKING SYSTEM")
    print("=" * 40)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Display All Accounts")
    print("7. Delete Account")
    print("8. Exit")
    print("=" * 40)


def main():

    bank = Bank()

    logger.info("Banking Application Started")

    while True:

        menu()

        try:

            choice = int(input("Enter your choice: "))

            match choice:

                case 1:

                    account_no = input("Enter Account Number: ").strip()
                    name = input("Enter Account Holder Name: ").strip()
                    balance = float(input("Enter Initial Balance: "))

                    bank.create_account(account_no, name, balance)

                case 2:

                    account_no = input("Enter Account Number: ").strip()
                    amount = float(input("Enter Deposit Amount: "))

                    bank.deposit(account_no, amount)

                case 3:

                    account_no = input("Enter Account Number: ").strip()
                    amount = float(input("Enter Withdraw Amount: "))

                    bank.withdraw(account_no, amount)

                case 4:

                    sender = input("Enter Sender Account: ").strip()
                    receiver = input("Enter Receiver Account: ").strip()
                    amount = float(input("Enter Transfer Amount: "))

                    bank.transfer(sender, receiver, amount)

                case 5:

                    account_no = input("Enter Account Number: ").strip()

                    bank.check_balance(account_no)

                case 6:

                    bank.display_accounts()

                case 7:

                    account_no = input("Enter Account Number: ").strip()

                    bank.delete_account(account_no)

                case 8:

                    logger.info("Application Closed")

                    print("\nThank you for using Secure Banking System.")

                    break

                case _:

                    logger.warning("Invalid Menu Choice")

                    print("Invalid Choice! Please try again.")

        except ValueError:

            logger.exception("Invalid Numeric Input")

            print("Please enter a valid number.")

        except KeyboardInterrupt:

            logger.warning("Program Interrupted by User")

            print("\nProgram Interrupted.")

            break

        except Exception:

            logger.exception("Unexpected Error")

            print("Something went wrong.")


if __name__ == "__main__":
    main()