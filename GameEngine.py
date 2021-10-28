from random import choice


class GameEngine:
    def __init__(self,):
        self.ai_choice = ''
        self.user_score = 0
        self.computer_score = 0

    def computer_choice(self):
        self.ai_choice = choice(["Rock", "Paper", "Scissors"])

    def who_win(self, usr_choice: str):
        if usr_choice == self.ai_choice:
            return "Draw"
        elif usr_choice == "Rock" and self.ai_choice == "Scissors" or usr_choice == "Paper" and self.ai_choice == "Rock" or usr_choice == "Scissors" and self.ai_choice == "Paper":
            self.user_score += 1
            return "You win!"
        elif usr_choice == "Rock" and self.ai_choice == "Paper" or usr_choice == "Paper" and self.ai_choice == "Scissors" or usr_choice == "Scissors" and self.ai_choice == "Rock":
            self.computer_score += 1
            return "You lose"

    def get_results(self):
        return self.user_score, self.computer_score


