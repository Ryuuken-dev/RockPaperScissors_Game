from View import View
from GameEngine import GameEngine


class Application:

    if __name__ == "__main__":
        view = View()
        games_number = view.game_numbers()
        usr_choice = view.users_choice()
        game_eng = GameEngine(games_number, usr_choice)
        for _ in range(games_number):
            pass
