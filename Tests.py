from View import View


class Tests:
    def __init__(self, view: View):
        self.view = view

    def test_if_user_specify_a_string_value_as_games_number(self):
        users_value = "asd"
        result = self.view.game_numbers()