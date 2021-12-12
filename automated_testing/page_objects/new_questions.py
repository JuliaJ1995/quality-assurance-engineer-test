from automated_testing.page_objects.page import Page


class NewQuestions(Page):

    def _new_questions(self):
        return self.browser.find_element_by_class_name('question-maker')

    def _add_question_button(self):
        return self.browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/form/button")

    def _new_question_input_field(self):
        return self.browser.find_element_by_id("question")

    def _new_answer_input_field(self):
        return self.browser.find_element_by_id("answer")

    def get_add_question_button_text(self):
        return self._add_question_button().text

    def click_add_question_button(self):
        return self._add_question_button().click()

    def _new_questions_title(self):
        return self._new_questions().find_element_by_tag_name('h2')

    def get_new_questions_tooltip(self):
        return self._new_questions().find_element_by_tag_name("span")

    def get_new_questions_title_text(self):
        return self._new_questions_title().text

    def insert_new_question(self, question_text):
        self._new_question_input_field().send_keys(question_text)

    def insert_new_answer(self, answer_text):
        self._new_answer_input_field().send_keys(answer_text)
