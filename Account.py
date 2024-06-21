import math
from typing import List


class Account:
    def __init__(self, balance: float, interest_rate: float, months: int):
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

    def calculate_interest(self) -> float:
        monthly_interest_rate = self.interest_rate / 12 / 100
        return round_down(
            self.balance * (1 + monthly_interest_rate) ** self.months - self.balance
        )


def round_down(number):
    return math.floor(number * 100) / 100
