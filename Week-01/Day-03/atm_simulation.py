# -----------------------------------------
# Day 03 Assignment
# ATM Simulation
# -----------------------------------------

# Step 1: Store the correct ATM PIN
correct_pin = "1234"

# Step 2: Store the initial account balance
balance = 5000

# Display welcome message
print("===================================")
print("       WELCOME TO ASSORT TECH ATM")
print("===================================")

# Step 3: Ask the user to enter the PIN
pin = input("Enter your 4-digit PIN: ")

# Step 4: Verify the PIN
if pin == correct_pin:

    print("\nLogin Successful!")
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Step 5: Ask the user to choose an option
    choice = input("\nEnter your choice (1-4): ")

    # -----------------------------
    # Option 1 - Check Balance
    # -----------------------------
    if choice == "1":
        print("\nYour Current Balance is: Rs.", balance)

    # -----------------------------
    # Option 2 - Deposit Money
    # -----------------------------
    elif choice == "2":

        deposit = float(input("Enter amount to deposit: Rs. "))

        # Add deposited amount to balance
        balance = balance + deposit

        print("Deposit Successful!")
        print("Updated Balance: Rs.", balance)

    # -----------------------------
    # Option 3 - Withdraw Money
    # -----------------------------
    elif choice == "3":

        withdraw = float(input("Enter amount to withdraw: Rs. "))

        # Check if balance is sufficient
        if withdraw <= balance:

            balance = balance - withdraw

            print("Withdrawal Successful!")
            print("Remaining Balance: Rs.", balance)

        else:
            print("Insufficient Balance!")

    # -----------------------------
    # Option 4 - Exit
    # -----------------------------
    elif choice == "4":
        print("Thank you for using Python ATM.")

    # -----------------------------
    # Invalid Menu Option
    # -----------------------------
    else:
        print("Invalid Choice!")

# Step 6: If PIN is incorrect
else:
    print("Incorrect PIN!")
    print("Access Denied!")

print("\n===================================")
print("Thank You!")
print("===================================")