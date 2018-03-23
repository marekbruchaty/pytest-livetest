# import pytest
# from account.account import Wallet, InsufficientAmount
#
#
# def test_default_initial_amount():
#     account = Wallet()
#     assert account.balance == 0
#
#
# def test_setting_initial_amount():
#     account = Wallet(100)
#     assert account.balance == 100
#
#
# def test_wallet_add_cash():
#     account = Wallet(10)
#     account.add_cash(90)
#     assert account.balance == 10
#
#
# def test_wallet_spend_cash():
#     account = Wallet(20)
#     account.spend_cash(10)
#     assert account.balance == 10
#
# def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
#     account = Wallet()
#     with pytest.raises(InsufficientAmount):
#         account.spend_cash(100)
