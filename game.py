from human import Human
from ai import AI

class Game:

    def __init__(self):
        self.player_one = None
        self.player_two = None

    # this is the funcion we call from main.py, it will call all the other funcion
    def run_game(self):
        self.intro()
        self.choose_mode()
        self.play_rounds()
        self.declare_winner()

    def intro(self):
        pass
    
    def choose_mode(self):
        user_choice = input("Press 1 for single player or 2 for multi-player")
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
    
    def play_rounds(self):
        pass

    def declare_winner(self):
        pass