import pytest
from bank_account.bank_account import BankAccount

not_an_account = 1

@pytest.fixture
def start_account():
    return BankAccount(100)

@pytest.fixture
def end_account():
    return BankAccount(100)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50

def test_transfer_to(start_account, end_account):
    start_account.transfer_to(end_account,50)
    assert start_account.balance == 50 and end_account.balance == 150

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount(-1)

def test_negative_withdraw_fails(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(-1)

def test_more_than_balance_withdraw_fails(start_account):
    with pytest.raises(ValueError):
        start_account.withdraw(101)

def test_negative_deposite_fails(start_account):
    with pytest.raises(ValueError):
        start_account.deposit(-1)

def test_target_not_bank_account_fails(start_account):
    with pytest.raises(ValueError):
        start_account.transfer_to(not_an_account,50)


