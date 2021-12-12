import pytest

from automated_testing.general.browser_actions import clear_browser, get_browser
from automated_testing.run_all_tests import URL


@pytest.fixture(autouse=True, scope='class')
def driver():
    """
    This function will be run with every test.
    At the beginning of each test, it will connect to Firefox browser and open page given in the URL variable.
    After tests is executed, with positive or negative result,
     this function will close and end the current browser session.
    """
    browser = get_browser()
    browser.get(URL)
    yield
    clear_browser()
