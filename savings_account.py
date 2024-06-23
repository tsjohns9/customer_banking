from Account import Account


class SavingsAccount(Account):
    def __init__(self, balance: float, interest_rate: float, months: int):
        super().__init__(balance, interest_rate, months)
        self.balance = balance
        self.interest_rate = interest_rate
        self.maturity_date = months
