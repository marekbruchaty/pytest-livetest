import unittest
from account.wallet import Wallet, InsufficientAmount


class TestWallet(unittest.TestCase):

    def test_default_initial_amount_dupl(self):
        import coverage

        cov = coverage.Coverage()
        cov.start()

        wallet = Wallet()
        self.assertTrue(wallet.balance == 0, "Initial balance not 0!")

        cov.stop()
        cov.save()

        cov.html_report()

    # def test_setting_initial_amount_not_zero_dupl(self):
    #     wallet = Wallet(100)
    #     self.assertTrue(wallet.balance == 100, "Initial balance wrong value!")
    #
    # def test_wallet_add_cash_dupl(self):
    #     wallet = Wallet(10)
    #
    #     self.assertTrue(wallet.balance == 100, "Wrong balance after funds received!")
    #     self.assertTrue(wallet.balance == 100, "Wrong balance after funds received!")
    #
    # def test_wallet_spend_cash_dupl(self):
    #     wallet = Wallet(20)
    #     wallet.spend_cash(10)
    #     self.assertTrue(wallet.balance == 10, "Wrong balance after funds spend!")
    #
    # def test_wallet_spend_cash_raises_exception_on_insufficient_amount_dupl(self):
    #     wallet = Wallet()
    #     with self.assertRaises(InsufficientAmount):
    #
    #         wallet.spend_cash(100)


if __name__ == '__main__':
    unittest.main()

