class InsufficientFundsError(Exception):
    """When a withdrawal does not go through due to insufficient funds"""
class BankAccount:
    def __init__(self, deposit: int):
        if deposit <= 0:
            raise ValueError("Opening deposit must be >= 0")
        self._balance = deposit
    # Returns the current account balance
    def get_balance(self):
        return self._balance
    # Adds the amount being deposited into the balance.
    def deposit(self, amount: int):
        if amount <= 0:
            return ValueError("Deposit amount must be >= 0")
        self._balance += amount
        return self.get_balance()
    # Need to prevent overdraft error
    # Returns the new balance
    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Withdraw amount must be >= 0")
        if amount > self._balance:
            raise InsufficientFundsError("Overdraft: Insufficient funds")
        self._balance -= amount
        return self.get_balance()