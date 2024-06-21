import csv
from typing import Dict

from Account import Account
from cd_account import CDAccount
from savings_account import SavingsAccount

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
account_types: Dict[str, Account] = {
    SAVINGS: SavingsAccount,
    CD: CDAccount,
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
    account: Account = account_types[account_type](balance, interest_rate, months)
    interest_earned = account.calculate_interest()
    updated_balance = account.balance + interest_earned
    print(
        f"The interest earned for the {account_type} account will be ${interest_earned:,.2f} after {months} months. The total balance will be ${updated_balance:,.2f}"
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
    print(
        f"How many months will you have the {account_type} account with this balance?"
    )
    while True:
        if account_type == SAVINGS:
            savings_maturity = select_number(
                f"Enter the number of months you will use the account. ",
                int,
                "Months",
            )
            for count, value in enumerate(savings_rates.values(), start=1):
                print(f"{count}. {value}% APY")
            choice = select_number(
                f"Select the interest rate for the savings account ",
                float,
                "Interest rate",
            )
            if choice > len(savings_rates):
                print(
                    f"\n{FAIL}Please select a valid number between 1 and {len(savings_rates)}.{END}\n"
                )
                continue
            return savings_maturity, savings_rates[choice]
        else:
            print(
                f"For a CD account, the following interest rates are available for the selected duration"
            )
            for count, (key, value) in enumerate(cd_months.items(), start=1):
                print(f"{count}. {key} months at {value}% APY")
            choice = select_number(
                f"Select the CD account you would like to open: ", int, "Interest rate"
            )
            if choice > len(cd_months):
                print(
                    f"\n{FAIL}Please select a valid number between 1 and {len(cd_months)}.{END}\n"
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
            print(f"\n{FAIL}{input_name} must be a number.{END}\n")


def print_invalid_value(key, value):
    print(f"\n{FAIL}{key} must be greater than {value}.{END}\n")


if __name__ == "__main__":
    main()
