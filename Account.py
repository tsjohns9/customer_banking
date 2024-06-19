""" Create a Account class with methods"""


class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest
