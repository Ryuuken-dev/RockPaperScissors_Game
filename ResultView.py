

class ResultView:

    @staticmethod
    def show_results(player_choice, computer_choice, result, points: tuple):
        print(f"User's Input: {player_choice}")
        print(f"Computer's Input: {computer_choice}\n")
        print(f'{result}\n')
        print(f'SCORE:\nUser Score: {points[0]}\tComputer Score: {points[1]}\n')
