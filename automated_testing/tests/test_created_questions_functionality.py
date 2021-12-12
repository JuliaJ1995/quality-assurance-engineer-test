import pytest

from automated_testing.page_objects.created_questions import CreatedQuestions
from automated_testing.page_objects.new_questions import NewQuestions
from automated_testing.page_objects.sidebar import Sidebar

data_set = [("xyz", "abc"), ("Trial question - what year is it?", "It's year 2021."), ("123", "456")]


@pytest.fixture(scope='class')
def add_question():
    for item in data_set:
        NewQuestions().insert_new_question(item[0])
        NewQuestions().insert_new_answer(item[1])
        NewQuestions().click_add_question_button()


@pytest.mark.usefixtures("add_question")
class TestCreatedQuestions:

    def test_sort_questions(self):
        manually_sorted_list = sorted([item.text for item in CreatedQuestions().get_list_of_created_questions()])
        CreatedQuestions().click_sort_questions_button()
        automatically_sorted_list = [item.text for item in CreatedQuestions().get_list_of_created_questions()]
        assert manually_sorted_list == automatically_sorted_list

    def test_number_of_questions_in_sidebar_text(self):
        number_of_questions = CreatedQuestions().get_number_of_created_questions()
        expected_msg = "Here you can find {} questions. " \
                       "Feel free to create your own questions!".format(number_of_questions)
        assert expected_msg == Sidebar().get_sidebar_text()

    @pytest.mark.parametrize("question_to_verify,expected_answer", data_set)
    def test_check_answer(self, question_to_verify, expected_answer):
        selected_question = None
        questions = CreatedQuestions().get_list_of_created_questions()
        for i, item in enumerate(questions):
            if item.text == question_to_verify:
                selected_question = questions[i]
                break
        selected_question.click()
        pre_existing_answer = CreatedQuestions().get_answer_to_specified_question(selected_question)
        assert expected_answer == pre_existing_answer
