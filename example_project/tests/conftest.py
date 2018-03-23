import coverage
import jsonpickle
import json
import re

cov = coverage.Coverage(cover_pylib=False, source=['/work/priv/python-test-samples'])
pickler = jsonpickle.pickler.Pickler(unpicklable=False)


# Add info to test report header
def pytest_report_header(config):
    return "livetest plugin active"


def pytest_runtest_setup(item):
    cov.start()  # Start coverage measurement
    item.runtest()  # Run current test case
    cov.stop()  # Stop coverage measurement

    data = cov.get_data()

    cov_map = [CoverageMapping(file, lines) for file, lines in data._lines.items() if
               not re.match(r".*__.*__\.py", file) and not re.match(r".*test_.*", file) and len(lines) > 0]

    tc_cov = pickler.flatten(TestCaseCoverage(item.name, cov_map), True)  # Pickle obj to json
    append_to_file("./some_file_random.txt", json.dumps(tc_cov) + "\n")  # Append to file for Java


def pytest_collection_modifyitems(config, items):
    pass


def append_to_file(filename, line):
    with open(filename, 'a') as file:
        file.write(line)


class CoverageMapping:
    def __init__(self, file_name, covered_lines):
        self.file_name = file_name
        self.covered_lines = covered_lines


class TestCaseCoverage:
    def __init__(self, test_name, coverage_mapping):
        self.test_name = test_name
        self.coverage_mapping = coverage_mapping
