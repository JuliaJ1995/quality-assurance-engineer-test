import pytest

from automated_testing.page_objects.created_questions import CreatedQuestions
from automated_testing.page_objects.sidebar import Sidebar


class TestRemoveQuestion:

    def test_remove_questions(self):
        CreatedQuestions().click_remove_questions_button()
        assert "No questions yet :-(" == CreatedQuestions().get_no_questions_message()

    @pytest.mark.depends(on=['test_remove_questions'])
    def test_no_questions_sidebar_info(self):
        assert "Here you can find no questions. Feel free to create your own questions!" == Sidebar().get_sidebar_text()
