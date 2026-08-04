# bank.py

import json
import os
from logger_config import logger


class Bank:

    def __init__(self, filename="accounts.json"):
        self.filename = filename
        self.accounts = {}
        self.load_accounts()

    # ----------------------------
    # Load Accounts
    # ----------------------------
    def load_accounts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.accounts = json.load(file)
                logger.info("Accounts loaded successfully.")
            except Exception as e:
                logger.exception("Failed to load accounts.")
                self.accounts = {}
        else:
            self.accounts = {}
            self.save_accounts()

    # ----------------------------
    # Save Accounts
    # ----------------------------
    def save_accounts(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.accounts, file, indent=4)
            logger.info("Accounts saved successfully.")
        except Exception:
            logger.exception("Error saving accounts.")

    # ----------------------------
    # Create Account
    # ----------------------------
    def create_account(self, account_no, name, balance):

        if account_no in self.accounts:
            logger.warning("Duplicate Account Attempt.")
            print("Account already exists.")
            return

        self.accounts[account_no] = {
            "name": name,
            "balance": balance
        }

        self.save_accounts()

        logger.info(f"Account Created -> {account_no}")

        print("Account created successfully.")

    # ----------------------------
    # Deposit
    # ----------------------------
    def deposit(self, account_no, amount):

        if account_no not in self.accounts:
            logger.error("Deposit Failed. Invalid Account.")
            print("Account not found.")
            return

        if amount <= 0:
            logger.error("Invalid Deposit Amount.")
            print("Amount must be greater than zero.")
            return

        self.accounts[account_no]["balance"] += amount

        self.save_accounts()

        logger.info(f"Deposit: {amount} into {account_no}")

        print("Deposit Successful.")

    # ----------------------------
    # Withdraw
    # ----------------------------
    def withdraw(self, account_no, amount):

        if account_no not in self.accounts:
            logger.error("Withdraw Failed. Invalid Account.")
            print("Account not found.")
            return

        balance = self.accounts[account_no]["balance"]

        if amount <= 0:
            logger.error("Invalid Withdraw Amount.")
            print("Amount must be greater than zero.")
            return

        if amount > balance:
            logger.error("Insufficient Balance.")
            print("Insufficient Balance.")
            return

        self.accounts[account_no]["balance"] -= amount

        self.save_accounts()

        logger.info(f"Withdraw: {amount} from {account_no}")

        print("Withdrawal Successful.")

    # ----------------------------
    # Transfer
    # ----------------------------
    def transfer(self, sender, receiver, amount):

        if sender not in self.accounts:
            print("Sender account not found.")
            logger.error("Sender Account Missing.")
            return

        if receiver not in self.accounts:
            print("Receiver account not found.")
            logger.error("Receiver Account Missing.")
            return

        if amount <= 0:
            print("Invalid Amount.")
            logger.error("Transfer Amount Invalid.")
            return

        if self.accounts[sender]["balance"] < amount:
            print("Insufficient Balance.")
            logger.error("Transfer Failed due to Balance.")
            return

        self.accounts[sender]["balance"] -= amount
        self.accounts[receiver]["balance"] += amount

        self.save_accounts()

        logger.info(
            f"Transfer: {amount} from {sender} to {receiver}"
        )

        print("Transfer Successful.")

    # ----------------------------
    # Check Balance
    # ----------------------------
    def check_balance(self, account_no):

        if account_no not in self.accounts:
            logger.error("Balance Check Failed.")
            print("Account not found.")
            return

        logger.info(f"Balance Checked -> {account_no}")

        print("\nName :", self.accounts[account_no]["name"])
        print("Balance :", self.accounts[account_no]["balance"])

    # ----------------------------
    # Display All Accounts
    # ----------------------------
    def display_accounts(self):

        if not self.accounts:
            print("No Accounts Found.")
            return

        print("\n------ All Accounts ------")

        for acc_no, details in self.accounts.items():

            print("-------------------------")
            print("Account :", acc_no)
            print("Name :", details["name"])
            print("Balance :", details["balance"])

    # ----------------------------
    # Delete Account
    # ----------------------------
    def delete_account(self, account_no):

        if account_no not in self.accounts:
            logger.error("Delete Failed.")
            print("Account not found.")
            return

        del self.accounts[account_no]

        self.save_accounts()

        logger.info(f"Deleted Account -> {account_no}")

        print("Account Deleted Successfully.")