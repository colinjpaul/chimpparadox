from account import Account, SecurityViolation
import pytest

b1 = Account('joe')
b2 = Account('sue')

def test_num_acs():
    assert Account.num_acs == 2
    #following appraoch is more object orientated
    assert Account.get_num_acs() == 2

def test_open_ac():
    assert isinstance(b1, Account)

def test_first_balance():
    assert b1.get_balance() == 0

def test_name():
    assert b1.name == 'joe'

def test_deposit():
    b1.deposit(100)
    assert b1.get_balance()==100

def test_first_trans():
    assert b1.trans[0] == 100
    assert b1[0] == 100

def test_change_trans():
    with pytest.raises(SecurityViolation):
        b1[0] = 200
        
def test_num_trans():
    assert len(b1) == 1







