from automated_testing.page_objects.page import Page


class Sidebar(Page):
    def _sidebar(self):
        return self.browser.find_element_by_class_name('sidebar')

    def get_sidebar_text(self):
        return self._sidebar().text
