from automated_testing.page_objects.page import Page


class CreatedQuestions(Page):
    def _created_questions(self):
        return self.browser.find_element_by_class_name('questions')

    def _created_questions_title(self):
        return self._created_questions().find_element_by_tag_name('h2')

    def _created_questions_list(self):
        return self._created_questions().find_element_by_tag_name("ul")

    def _sort_questions_button(self):
        return self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[2]/button[1]")

    def _remove_questions_button(self):
        return self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/div[2]/button[2]")

    def _no_questions_info(self):
        return self._created_questions().find_element_by_xpath("div[2]")

    def get_no_questions_message(self):
        return self._no_questions_info().text

    def get_created_questions_title_text(self):
        return self._created_questions_title().text

    def get_sort_questions_button_text(self):
        return self._sort_questions_button().text

    def click_sort_questions_button(self):
        return self._sort_questions_button().click()

    def get_remove_questions_button_text(self):
        return self._remove_questions_button().text

    def click_remove_questions_button(self):
        return self._remove_questions_button().click()

    def get_number_of_created_questions(self):
        return self._created_questions_list().get_attribute('childElementCount')

    def get_list_of_created_questions(self):
        return self._created_questions_list().find_elements_by_tag_name("li")

    def get_created_questions_tooltip(self):
        return self._created_questions().find_element_by_tag_name("span")

    def get_answer_to_specified_question(self, question_locator):
        return question_locator.find_element_by_tag_name("p").text
