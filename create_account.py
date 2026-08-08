from account import Account
from account_data import accounts


def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    account_id = input("Enter Account ID: ")

    # Check duplicate Account ID
    for account in accounts:
        if account.account_id == account_id:
            print("Account ID already exists!")
            print("Please use a different Account ID.")
            return

    name = input("Enter Account Holder Name: ")

    try:
        balance = float(input("Enter Initial Deposit: ₹"))

        if balance < 0:
            print("Initial deposit cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    new_account = Account(account_id, name, balance)

    accounts.append(new_account)

    print("\nAccount created successfully!")
    print("Account ID :", new_account.account_id)
    print("Name       :", new_account.name)
    print("Balance    : ₹{:.2f}".format(new_account.balance))