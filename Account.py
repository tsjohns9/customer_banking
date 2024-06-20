""" Create a Account class with methods"""


class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Account balance: ${self.balance:.2f}")


class SavingsAccount(Account):
    def __init__(self, pin, balance=0.0, interest_rate=0.01):
        super().__init__(pin, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self, years):
        self.balance += self.balance * self.interest_rate * years
        self.transactions.append(
            (
                "Interest",
                self.balance * self.interest_rate * years,
                datetime.datetime.now(),
            )
        )
        print(
            f"Interest accrued over {years} year(s): ${self.balance * self.interest_rate * years:.2f}"
        )


class CDAccount(Account):
    def __init__(self, pin, balance=0.0, interest_rate=0.03, term=1):
        super().__init__(pin, balance)
        self.interest_rate = interest_rate
        self.term = term
        self.start_date = datetime.datetime.now()
        self.maturity_date = self.start_date + datetime.timedelta(days=365 * self.term)

    def calculate_interest(self):
        if datetime.datetime.now() >= self.maturity_date:
            self.balance += self.balance * self.interest_rate * self.term
            self.transactions.append(
                (
                    "Interest",
                    self.balance * self.interest_rate * self.term,
                    datetime.datetime.now(),
                )
            )
            print(
                f"Interest accrued over {self.term} year(s): ${self.balance * self.interest_rate * self.term:.2f}"
            )
        else:
            print(f"CD has not matured yet. Maturity date is {self.maturity_date}")

    def withdraw(self, amount):
        if datetime.datetime.now() >= self.maturity_date:
            super().withdraw(amount)
        else:
            print("Cannot withdraw funds before the maturity date")
