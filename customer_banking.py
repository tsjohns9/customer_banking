from cd_account import create_cd_account
from savings_account import create_savings_account

FAIL = "\033[91m"
END = "\033[0m"
SAVINGS = "savings"
CD = "CD"

opts = {
    1: SAVINGS,
    2: CD,
}
funcs = {
    SAVINGS: create_savings_account,
    CD: create_cd_account,
}
cd_months = {
    12: 4.35,
    24: 4.00,
    36: 3.00,
    48: 3.00,
    60: 3.00,
}


def main():
    print("Welcome to the banking app!")
    account_type = select_account()
    balance = select_number(
        f"How much would you like to deposit into the {account_type}? ",
        float,
        "Balance",
    )
    savings_maturity, interest = select_months_interest(account_type)
    updated_balance, interest_earned = funcs[account_type](
        balance,
        interest,
        savings_maturity,
    )
    print("updated_balance", updated_balance)
    print("interest_earned", interest_earned)
    print(
        f"The interest earned for the {account_type} account is {interest_earned}% for {savings_maturity} months. The total balance is now {updated_balance}"
    )


def select_account():
    while True:
        print("1. Manage savings account")
        print("2. Manage CD account")
        choice = input("What would you like to do? ")
        if choice.isdigit() and 1 <= int(choice) <= 2:
            return opts[int(choice)]
        print(f"\n{FAIL}Invalid Option, please try again{END}\n")


def select_months_interest(account_type):
    print("How many months will you have the {account_type} with this balance?")
    while True:
        if account_type == SAVINGS:
            savings_maturity = select_number(
                f"The interest rate is 0.01% APY for a savings account. Enter the number of months you will use the account. ",
                int,
                "Months",
            )
            interest = 0.01
            return savings_maturity, interest
        else:
            print(
                f"For a CD account, the following interest rates are available for the selected duration"
            )
            for count, (key, value) in enumerate(cd_months.items(), start=1):
                print(f"{count}. {key} at {value}% APY")
            choice = select_number(
                f"Select the CD account you would like to open: ", int, "Interest rate"
            )
            if choice > len(cd_months):
                print(
                    f"\n{FAIL}Please select a valid number between 1 and {len(cd_months)} {value}.{END}\n"
                )
                continue

            maturity = None
            interest = None
            for index, (key, value) in enumerate(cd_months.items(), start=1):
                if index == choice:
                    maturity = key
                    interest = value
            print("maturity, interest", maturity, interest)
            return maturity, interest


def select_number(prompt, type, input_name):
    while True:
        try:
            balance = type(input(prompt))
            if balance <= 0:
                print_invalid_value(input_name, 0)
            else:
                return balance
        except ValueError:
            print_invalid_type(input_name, "number")


def print_invalid_value(key, value):
    print(f"\n{FAIL}{key} must be greater than {value}.{END}\n")


def print_invalid_type(key, value):
    print(f"\n{FAIL}{key} must be a {value}.{END}\n")


if __name__ == "__main__":
    main()
