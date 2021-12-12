import pytest

# Url used for all test cases
URL = "localhost:8000"
# Browser used to run automated tests
browser_type = 'Firefox'
# Directory containing tests that should be run is defined
directory_with_tests = ['tests/']
# All files that start with "test" will be found in the given directory and all of them will be executed one by one
pytest.main(directory_with_tests)
