import datetime
import math
from typing import List


class Account:
    def __init__(self, pin: int, balance: float, interest_rate: float, months: int):
        self.pin: int = pin
        self.balance: float = balance
        self.interest_rate: float = interest_rate
        self.months = months
        self.transactions: List[float] = []

    def set_balance(self, balance):
        self.balance = balance

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

    def calculate_interest() -> float:
        pass


class SavingsAccount(Account):
    def __init__(self, pin: int, balance: float, interest_rate: float, months: int):
        super().__init__(pin, balance, interest_rate, months)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        monthly_interest_rate = self.interest_rate / 12 / 100
        return round_down(
            self.balance * (1 + monthly_interest_rate) ** self.months - self.balance
        )

    def withdraw(self):
        pass


class CDAccount(Account):
    def __init__(self, pin: int, balance: float, interest_rate: float, months: int):
        super().__init__(pin, balance, interest_rate, months)
        self.balance = balance
        self.interest_rate = interest_rate
        self.start_date = datetime.datetime.now()
        self.maturity_date = months

    def calculate_interest(self) -> float:
        monthly_interest_rate = self.interest_rate / 12 / 100
        return round_down(
            self.balance * (1 + monthly_interest_rate) ** self.months - self.balance
        )

    def withdraw(self, amount):
        pass


def round_down(number):
    return math.floor(number * 100) / 100
