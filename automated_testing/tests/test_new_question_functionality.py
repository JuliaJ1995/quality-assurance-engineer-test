import pytest

from automated_testing.page_objects.created_questions import CreatedQuestions
from automated_testing.page_objects.new_questions import NewQuestions


class TestNewQuestion:

    data_set = [("q1", "a1"), ("q2", "a2"), ("new question", "new answer")]

    @pytest.mark.parametrize("question,answer", data_set)
    def test_add_question(self, question, answer):
        initial_number_of_questions = CreatedQuestions().get_number_of_created_questions()
        NewQuestions().insert_new_question(question)
        NewQuestions().insert_new_answer(answer)
        NewQuestions().click_add_question_button()
        expected_number_of_questions = int(initial_number_of_questions) + 1
        assert str(expected_number_of_questions) == CreatedQuestions().get_number_of_created_questions()
