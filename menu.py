from create_account import create_account
from deposit import deposit
from withdraw import withdraw
from balance import check_balance


def show_menu():

    while True:

        print("\n")
        print("======================================")
        print("       BANKING MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Check")
        print("5. Exit")
        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            print("\nThank you for using Banking System!")
            break

        else:
            print("Invalid choice! Please try again.")