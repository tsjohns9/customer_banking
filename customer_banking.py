from typing import Dict

from cd_account import create_cd_account
from savings_account import create_savings_account

FAIL = "\033[91m"
END = "\033[0m"
SAVINGS = "savings"
CD = "CD"
csv_file_path = "./accounts.csv"

opts: Dict[int, str] = {
    1: SAVINGS,
    2: CD,
}

savings_rates: Dict[int, float] = {
    1: 0.01,
    2: 0.02,
    3: 0.03,
}

cd_months: Dict[int, float] = {
    12: 4.35,
    24: 4.00,
    36: 3.50,
    48: 3.25,
    60: 3.00,
}
account_types = {
    SAVINGS: create_savings_account,
    CD: create_cd_account,
}


def main():
    print("Welcome to the banking app!")
    account_type = select_account()
    balance = select_number(
        f"How much would you like to deposit into the {account_type}? ",
        float,
        "Balance",
    )
    months, interest_rate = select_months_interest(account_type)
    balance_with_interest, interest_earned = account_types[account_type](
        balance, interest_rate, months
    )
    print(
        f"The interest earned for the {account_type} account will be "
        f"${interest_earned:,.2f} after {months} months. "
        f"The total balance will be ${balance_with_interest:,.2f}"
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
    maturity = select_number(
        f"Enter the total number of months to hold the {account_type} account: ",
        int,
        "months",
    )
    interest = select_number(
        f"Enter the interest rate for the {account_type} account: ",
        float,
        "interest rate",
    )
    return maturity, interest


def select_number(prompt, type, input_name):
    while True:
        try:
            num = type(input(prompt))
            if num <= 0:
                print_invalid_value(input_name, 0)
            else:
                return num
        except ValueError:
            print(f"\n{FAIL}{input_name} must be a number.{END}\n")


def print_invalid_value(key, value):
    print(f"\n{FAIL}{key} must be greater than {value}.{END}\n")


if __name__ == "__main__":
    main()
