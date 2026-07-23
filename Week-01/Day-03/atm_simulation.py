# -----------------------------------------
# Day 03 Assignment
# ATM Simulation (Improved Version)
# -----------------------------------------

# ATM Data
correct_pin = "1234"
balance = 5000
max_attempts = 3

print("===================================")
print("      WELCOME TO ASSORT TECH ATM")
print("===================================")

# ----------------------------
# PIN Verification
# ----------------------------
attempt = 0

while attempt < max_attempts:

    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:

        print("\nLogin Successful!")

        # ----------------------------
        # ATM Menu
        # ----------------------------
        while True:

            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("\nEnter your choice (1-4): ")

            match choice:

                # ----------------------------
                # Check Balance
                # ----------------------------
                case "1":
                    print(f"\nCurrent Balance: Rs. {balance}")

                # ----------------------------
                # Deposit Money
                # ----------------------------
                case "2":

                    try:
                        deposit = float(input("Enter amount to deposit: Rs. "))

                        if deposit <= 0:
                            print("Invalid amount! Deposit must be greater than 0.")

                        else:
                            balance += deposit
                            print("Deposit Successful!")
                            print(f"Updated Balance: Rs. {balance}")

                    except ValueError:
                        print("Invalid input! Please enter numbers only.")

                # ----------------------------
                # Withdraw Money
                # ----------------------------
                case "3":

                    try:
                        withdraw = float(input("Enter amount to withdraw: Rs. "))

                        if withdraw <= 0:
                            print("Invalid amount! Withdrawal must be greater than 0.")

                        elif withdraw > balance:
                            print("Insufficient Balance!")

                        else:
                            balance -= withdraw
                            print("Withdrawal Successful!")
                            print(f"Remaining Balance: Rs. {balance}")

                    except ValueError:
                        print("Invalid input! Please enter numbers only.")

                # ----------------------------
                # Exit
                # ----------------------------
                case "4":
                    print("\nThank you for using Assort Tech ATM.")
                    print("Have a Nice Day!")
                    break

                # ----------------------------
                # Invalid Choice
                # ----------------------------
                case _:
                    print("Invalid Choice! Please select between 1 and 4.")

        # Exit the PIN loop after user exits ATM
        break

    else:
        attempt += 1
        remaining = max_attempts - attempt

        if remaining > 0:
            print(f"Incorrect PIN! Attempts left: {remaining}")

        else:
            print("\nToo many incorrect attempts!")
            print("Your account has been temporarily locked.")

print("\n===================================")
print("         THANK YOU")
print("===================================")
