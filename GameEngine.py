from random import choice

#Użycie dziedziczenia z klasy View

class GameEngine:
    def __init__(self, number_of_games: int, users_input: str):
        self.users_input = users_input
        self.number_of_games = number_of_games
        self.ai_choice = ''

    def computer_choice(self):
        self.ai_choice = choice(["Rock", "Paper", "Scissors"])

    def get_result(self):
        if self.users_input == self.ai_choice:
            return "Draw"
        elif self.users_input == "Rock" and self.ai_choice == "Scissors" or self.users_input == "Paper" and self.ai_choice == "Rock" or self.users_input == "Scissors" and self.ai_choice == "Paper":
            return "You win!"
        elif self.users_input == "Rock" and self.ai_choice == "Paper" or self.users_input == "Paper" and self.ai_choice == "Scissors" or self.users_input == "Scissors" and self.ai_choice == "Rock":
            return "You lose"
