import pytest
from Bank import Bank 


## Test Cases
def test_bank():
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10) == True
    assert bank.transfer(5, 1, 20) == True
    assert bank.deposit(5, 20) == True
    assert bank.transfer(3, 4, 15) == False
    assert bank.withdraw(10, 50) == False

    bank = Bank([0, 0, 0])
    assert bank.withdraw(1, 1) == False
    assert bank.transfer(1, 2, 1) == False
    assert bank.deposit(3, 50) == True
    assert bank.withdraw(3, 10) == True
    assert bank.transfer(3, 1, 20) == True
    assert bank.deposit(5, 100) == False

def test_invalid_account(): 
    bank = Bank([100, 200, 300])
    assert bank.withdraw(0, 50) == False
    assert bank.withdraw(4, 50) == False
    assert bank.deposit(0, 50) == False
    assert bank.deposit(4, 50) == False
    assert bank.transfer(0, 2, 50) == False
    assert bank.transfer(1, 5, 50) == False

def test_negative_amounts():
    bank = Bank([100, 200, 300])
    assert bank.withdraw(1, -50) == False
    assert bank.deposit(2, -50) == False
    assert bank.transfer(1, 2, -50) == False

def test_insufficient_funds():
    bank = Bank([100, 200, 300])
    assert bank.withdraw(1, 150) == False
    assert bank.transfer(1, 2, 150) == False

def test_edge_cases():
    bank = Bank([0])
    assert bank.deposit(1, 0) == True
    assert bank.withdraw(1, 0) == True
    assert bank.transfer(1, 1, 0) == True


if __name__ == "__main__":
    pytest.main()
