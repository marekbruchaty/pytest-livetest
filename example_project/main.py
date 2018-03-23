import jsonpickle
pickler = jsonpickle.pickler.Pickler(unpicklable=False)


class CoverageMapping:
    def __init__(self, file_name, covered_lines):
        self.file_name = file_name
        self.covered_lines = covered_lines


class TestCaseCoverage:
    def __init__(self, test_name, coverage_mapping):
        self.test_name = test_name
        self.coverage_mapping = coverage_mapping


def main():
    # print("start")
    #
    # wallet = Wallet()
    #
    # wallet.add_cash(10000)
    # wallet.spend_cash(9000)
    #
    # print(wallet.balance)
    #
    # print("end")

    covered_lines = {u'/work/priv/python-test-samples/account/wallet.py': [7],
                     u'/work/priv/python-test-samples/playground.py': [],
                     u'/work/priv/python-test-samples/account/__main__.py': [],
                     u'/work/priv/python-test-samples/tests/test_wallet_pytest.py': [6, 7],
                     u'/work/priv/python-test-samples/tests/__init__.py': [],
                     u'/work/priv/python-test-samples/tests/conftest.py': [],
                     u'/work/priv/python-test-samples/tests/test_wallet_unittest_duplicate.py': [],
                     u'/work/priv/python-test-samples/tests/test_wallet_unittest.py': [],
                     u'/work/priv/python-test-samples/account/__init__.py': [],
                     u'/work/priv/python-test-samples/main.py': []}

    test_case_cov = TestCaseCoverage('nejaky test',
                                     [CoverageMapping(file, lines) for file, lines in covered_lines.items()])

    serialized_tc_coverage = pickler.flatten(test_case_cov, True)
    print(serialized_tc_coverage)


if __name__ == '__main__':
    main()
