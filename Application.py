from View import View
from GameEngine import GameEngine
from ResultView import ResultView


class Application:

    if __name__ == "__main__":
        view = View()
        games_number = view.game_numbers()
        game_eng = GameEngine()
        res_view = ResultView()
        for _ in range(games_number):
            usr_choice = view.users_choice()
            ai_choice = game_eng.computer_choice()
            winner = game_eng.who_win(usr_choice)
            results = game_eng.get_results()
            res_view.show_results(usr_choice, game_eng.ai_choice, winner, results)
