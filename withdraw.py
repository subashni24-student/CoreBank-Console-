from account_data import accounts


def withdraw():

    print("\n========== WITHDRAW ==========")

    account_id = input("Enter Account ID: ")

    # Search account using for loop
    for account in accounts:

        if account.account_id == account_id:

            try:
                amount = float(input("Enter Withdrawal Amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    return

            except ValueError:
                print("Please enter a valid amount.")
                return

            # Check balance
            if amount > account.balance:
                print("Insufficient balance.")
                return

            # Update balance
            account.balance = account.balance - amount

            print("\nWithdrawal successful!")
            print("Withdrawn Amount : ₹{:.2f}".format(amount))
            print("Current Balance  : ₹{:.2f}".format(account.balance))

            return

    print("Account not found.")