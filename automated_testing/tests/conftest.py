import pytest

from automated_testing.general.browser_actions import clear_browser, get_browser
from automated_testing.run_all_tests import URL


@pytest.fixture(autouse=True, scope='class')
def driver():
    """
    This function will be run for every test class.
    At the beginning of each test set (tests defined in one class),
    it will connect to the defined browser and open page given in the URL variable.
    After all tests from the class are executed, with positive or negative results,
    this function will close and end the current browser session.
    """
    browser = get_browser()
    browser.get(URL)
    yield
    clear_browser()
