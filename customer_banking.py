import csv

from Account import Account, CDAccount, SavingsAccount

FAIL = "\033[91m"
END = "\033[0m"
SAVINGS = "savings"
CD = "CD"
csv_file_path = "./accounts.csv"

opts = {
    1: SAVINGS,
    2: CD,
}

cd_months = {
    12: 4.35,
    24: 4.00,
    36: 3.50,
    48: 3.25,
    60: 3.00,
}
account_types = {
    SAVINGS: SavingsAccount,
    CD: CDAccount,
}


def main():
    print("Welcome to the banking app!")
    accounts = read_accounts()
    pin: int = None
    if len(accounts) == 0:
        pin = create_pin()

    account_type = select_account()
    balance = select_number(
        f"How much would you like to deposit into the {account_type}? ",
        float,
        "Balance",
    )
    months, interest_rate = select_months_interest(account_type)
    account: Account = account_types[account_type](pin, balance, interest_rate, months)
    interest_earned = account.calculate_interest()
    updated_balance = account.balance + interest_earned
    print(
        f"The interest earned for the {account_type} account will be ${interest_earned:,.2f} after {months} months. The total balance will be ${updated_balance:,.2f}"
    )

    write_account(account, account_type, months)


def read_accounts():
    accounts = []
    with open(csv_file_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 0:
                continue
            if row[1] == "cd":
                accounts.append(
                    CDAccount(
                        pin=row[0],
                        balance=row[2],
                        interest_rate=row[3],
                        months=row[4],
                    )
                )
            elif row[1] == "savings":
                accounts.append(
                    CDAccount(
                        pin=row[0],
                        balance=row[2],
                        interest_rate=row[3],
                        months=row[4],
                    )
                )
    return accounts


def write_account(account: Account, account_type: str, months: int):
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                account.pin,
                account_type,
                account.balance,
                account.interest_rate,
                account.months,
            ]
        )


def create_pin() -> int:
    while True:
        pin = select_number(
            "Please enter a 4 digit PIN to create an account: ",
            int,
            "PIN",
        )
        if pin < 1000:
            print(f"\n{FAIL}PIN must be 4 digits.{END}\n")
            continue
        print("Save this pin so that you can log into your account next time.")
        return pin


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
                print(f"{count}. {key} months at {value}% APY")
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
            print(f"\n{FAIL}{input_name} must be a number.{END}\n")


def print_invalid_value(key, value):
    print(f"\n{FAIL}{key} must be greater than {value}.{END}\n")


if __name__ == "__main__":
    main()
