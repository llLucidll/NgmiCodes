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

        account -= 1 
        if money < 0 or self.balance[account] < money:
            return False 

        self.balance[account] -= money
        return True 
    

# Write a CLI interface to interact with the Bank class
if __name__ == "__main__":
    bank = Bank([100, 200, 300])
    while True:
        print("\nOptions:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            account = int(input("Enter account number: "))
            amount = int(input("Enter amount to withdraw: "))
            if bank.withdraw(account, amount):
                print(f"Withdrew {amount} from account {account}.")
            else:
                print("Withdrawal failed.")
        
        elif choice == '2':
            account = int(input("Enter account number: "))
            amount = int(input("Enter amount to deposit: "))
            if bank.deposit(account, amount):
                print(f"Deposited {amount} to account {account}.")
            else:
                print("Deposit failed.")
        
        elif choice == '3':
            account1 = int(input("Enter source account number: "))
            account2 = int(input("Enter destination account number: "))
            amount = int(input("Enter amount to transfer: "))
            if bank.transfer(account1, account2, amount):
                print(f"Transferred {amount} from account {account1} to account {account2}.")
            else:
                print("Transfer failed.")
        
        elif choice == '4':
            for i, bal in enumerate(bank.balance, start=1):
                print(f"Account {i}: Balance {bal}")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")        
