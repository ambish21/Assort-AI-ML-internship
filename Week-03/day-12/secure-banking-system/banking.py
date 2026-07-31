from exceptions import InvalidAmountError, InsufficientBalanceError


class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than 0.")

        self.balance += amount
        print(f"\nRs.{amount} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0.")

        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        self.balance -= amount
        print(f"\nRs.{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"\nCurrent Balance: Rs.{self.balance}")


def main():

    account = BankAccount()

    while True:

        print("\n========== Secure Banking System ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":

                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            elif choice == "2":

                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == "3":

                account.check_balance()

            elif choice == "4":

                print("\nThank you for using Secure Banking System.")
                break

            else:

                print("\nInvalid menu choice.")

        except ValueError:
            print("\nPlease enter numbers only.")

        except InvalidAmountError as e:
            print(f"\nError: {e}")

        except InsufficientBalanceError as e:
            print(f"\nError: {e}")

        except Exception as e:
            print(f"\nUnexpected Error: {e}")

        finally:
            print("\nTransaction Finished.")


if __name__ == "__main__":
    main()