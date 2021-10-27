class View:
    def __init__(self):
        self.number_of_games = 0
        self.users_input = ''

    def game_numbers(self):
        try:
            self.number_of_games = int(input('Enter the number of games you want to play: '))
        except ValueError:
            proper_value = int(input('Enter proper value (number greater than 0): '))
            self.number_of_games = proper_value
        while self.number_of_games < 0:
            proper_number = int(input("You can't a number lower than 0: "))
            self.number_of_games = proper_number
        return self.number_of_games

    def users_choice(self):
        proper_values = ("Rock", "Paper", "Scissors")
        self.users_input = str(input("User's Input (Available options: Rock, Paper, Scissors): "))
        while self.users_input not in proper_values:
            get_value = str(input('Enter a proper value from available options: '))
            self.users_input = get_value
        return self.users_input

