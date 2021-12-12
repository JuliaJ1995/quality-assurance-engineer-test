from automated_testing.general.browser_actions import get_browser


class Page:

    def __init__(self):
        self.browser = get_browser()
