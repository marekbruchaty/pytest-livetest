from account.wallet import Wallet


def main():
    print("start")

    wallet = Wallet()

    wallet.add_cash(10000)
    wallet.spend_cash(9000)

    print(wallet.balance)

    print("end")


if __name__ == '__main__':
    main()
