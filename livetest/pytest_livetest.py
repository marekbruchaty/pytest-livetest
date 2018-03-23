def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("setting up", item)
    append_to_file("/work/priv/pytest-livetest/some_file_random.txt", "working")


def append_to_file(filename, line):
    with open(filename, 'a') as file:
        file.write(line)
