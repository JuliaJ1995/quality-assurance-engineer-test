from automated_testing.page_objects.created_questions import CreatedQuestions
from automated_testing.page_objects.header import Header
from automated_testing.page_objects.new_questions import NewQuestions
from automated_testing.page_objects.sidebar import Sidebar


class TestInitialLayout:
    def test_header_title(self):
        assert "The awesome Q/A tool" == Header().get_title_text()

    def test_sidebar_text(self):
        text = Sidebar().get_sidebar_text()
        assert "Here you can find 1 question. Feel free to create your own questions!" == text

    def test_created_questions_title(self):
        text = CreatedQuestions().get_created_questions_title_text()
        assert 'Created questions' == text

    def test_created_questions_tooltip(self):
        tooltip_text = CreatedQuestions().get_created_questions_tooltip().get_attribute("innerHTML")
        assert "Here you can find the created questions and their answers." == tooltip_text

    def test_count_questions(self):
        text = CreatedQuestions().get_number_of_created_questions()
        assert '1' == text

    def test_pre_existing_question_text(self):
        pre_existing_question = CreatedQuestions().get_list_of_created_questions()[0]
        assert "How to add a question?" == pre_existing_question.text

    def test_pre_existing_answer_is_not_accessible(self):
        pre_existing_question = CreatedQuestions().get_list_of_created_questions()[0]
        assert "" == CreatedQuestions().get_answer_to_specified_question(pre_existing_question)

    def test_click_to_access_answer(self):
        pre_existing_question = CreatedQuestions().get_list_of_created_questions()[0]
        pre_existing_question.click()
        pre_existing_answer = CreatedQuestions().get_answer_to_specified_question(pre_existing_question)
        assert "Just use the form below!" == pre_existing_answer

    def test_sort_questions_button_text(self):
        assert 'Sort questions' == CreatedQuestions().get_sort_questions_button_text()

    def test_remove_questions_button_text(self):
        assert 'Remove questions' == CreatedQuestions().get_remove_questions_button_text()

    def test_new_questions_title(self):
        assert 'Create a new question' == NewQuestions().get_new_questions_title_text()

    def test_new_questions_tooltip(self):
        tooltip_text = NewQuestions().get_new_questions_tooltip().get_attribute("innerHTML")
        assert "Here you can create new questions and their answers." == tooltip_text

    def test_create_question_button_text(self):
        assert 'Create question' == NewQuestions().get_add_question_button_text()
