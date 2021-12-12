from automated_testing.page_objects.page import Page


class Header(Page):
    def _title(self):
        return self.browser.find_element_by_tag_name('h1')

    def get_title_text(self):
        return self._title().text
