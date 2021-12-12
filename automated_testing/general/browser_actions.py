from selenium import webdriver
from automated_testing.run_all_tests import browser_type

_browser = None


def get_browser():
    """
    Function which checks if global variable _browser is assigned.
    If it is then already existing WebDriver instance is returned. If not then new instance is created and returned.
    :return: WebDriver instance is returned
    """
    global _browser
    if _browser:
        return _browser
    else:
        _browser = setup_browser()
        return _browser


def setup_browser():
    """
    Function which creates new WebDriver instance for selected browser and maximizes the browser window.
    Currently, only Firefox browser is supported but more can be added as options in the match statement.
    :return: new WebDriver instance
    """
    match browser_type:
        case 'Firefox':
            browser = webdriver.Firefox()
        case _:
            browser = webdriver.Firefox()
    browser.maximize_window()
    return browser


def clear_browser():
    """
    Function which closes the browser window and ends current WebDriver instance. Global variable _browser is cleared.
    """
    global _browser
    get_browser().close()
    get_browser().quit()
    _browser = None
