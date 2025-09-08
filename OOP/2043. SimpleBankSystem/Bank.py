class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance 
    
    def is_valid(self, account):
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.withdraw(account1, money):
            return False 
        
        if not self.deposit(account2, money):
            self.deposit(account1, money)
            return False 

        return True 

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False 
        
        if money < 0:
            return False 

        account -= 1
        self.balance[account] += money
        return True 


    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False 

        if money < 0 or self.balance[account] < money:
            return False 

        account -= 1 
        self.balance[account] -= money
        return True 
    

        
