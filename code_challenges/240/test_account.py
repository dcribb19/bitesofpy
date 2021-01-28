import pytest

from account import Account

bob = Account('Bob')
dcribb19 = Account('Daniel', 500)


def test_init():
    assert dcribb19.owner == 'Daniel'
    assert dcribb19.amount == 500
    assert dcribb19._transactions == []


def test_repr():
    assert repr(bob) == "Account('Bob', 0)"


def test_str():
    assert str(bob) == 'Account of Bob with starting amount: 0'


def test_add_transaction():
    bob.add_transaction(100)
    assert bob._transactions == [100]


def test_add_transaction_invalid_input():
    with pytest.raises(ValueError) as e:
        bob.add_transaction('So much money')
    assert('please use int for amount') in str(e.value)


def test_balance():
    assert bob.balance == 100
    bob.add_transaction(200)
    assert bob.balance == 300


def test_len_transactions():
    assert len(bob) == 2
    bob.add_transaction(50)
    assert len(bob) == 3


def test_getitem():
    assert bob.__getitem__(2) == 50


def test_balance_comparison():
    assert bob < dcribb19
    assert bob <= dcribb19
    assert dcribb19 > bob
    assert dcribb19 >= bob
    bob.add_transaction(150)
    assert bob == dcribb19


def test_add():
    bd = bob.__add__(dcribb19)
    assert bd.owner == 'Bob&Daniel'
    assert bd.balance == 1_000
