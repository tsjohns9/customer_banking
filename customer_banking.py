from cd_account import create_cd_account
from savings_account import create_savings_account

FAIL = "\033[91m"
END = "\033[0m"


def main():
    opts = {
        1: "savings",
        2: "CD",
    }
    funcs = {
        1: create_savings_account,
        2: create_cd_account,
    }

    print("Welcome to the banking app!")
    choice = None
    while True:
        print("1. Manage savings account")
        print("2. Manage CD account")
        choice = input("What would you like to do? ")
        if choice.isdigit() and 1 <= int(choice) <= 2:
            choice = int(choice)
            break
        print(f"\n{FAIL}Invalid Option, please try again{END}\n")

    while True:
        balance = None
        interest = None
        try:
            balance = float(input(f"What is the {opts[choice]} balance? "))
            if balance <= 0:
                print_invalid_value("Balance", 0)
                continue
        except ValueError:
            print_invalid_type("Balance", "integer or a float")
            continue

        try:
            interest = float(
                input(f"What is the interest rate for the {opts[choice]} account? ")
            )
            if interest <= 0:
                print_invalid_value("Interest rate", 0)
                continue
        except ValueError:
            print_invalid_type("Interest rate", "integer or a float")
            continue

        savings_maturity = input("How many months will the account have this total? ")
        if savings_maturity.isdigit():
            savings_maturity = int(savings_maturity)
            if savings_maturity <= 0:
                print_invalid_value("Months rate", 0)
                continue
        else:
            print(f"\n{FAIL}Months must be an integer.{END}\n")
            print_invalid_type("Months", "integer")
            continue

        updated_balance, interest_earned = funcs[choice](
            balance,
            interest,
            savings_maturity,
        )
        print(
            f"The interest earned for the {opts[choice]} account is {interest_earned}% for {savings_maturity} months. The total balance is now {updated_balance}"
        )


def print_invalid_value(key, value):
    print(f"\n{FAIL}{key} must be greater than {value}.{END}\n")


def print_invalid_type(key, value):
    print(f"\n{FAIL}{key} must be an {value}.{END}\n")


if __name__ == "__main__":
    main()
