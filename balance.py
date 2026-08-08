from account_data import accounts


def check_balance():

    print("\n========== BALANCE CHECK ==========")

    account_id = input("Enter Account ID: ")

    # Search account using for loop
    for account in accounts:

        if account.account_id == account_id:

            print("\nAccount ID : ", account.account_id)
            print("Name       : ", account.name)
            print("Balance    : ₹{:.2f}".format(account.balance))

            return

    print("Account not found.")