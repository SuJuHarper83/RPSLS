from human import Human
from ai import AI

class Game:

    def __init__(self):
        self.player_one = ()
        self.player_two = ()

    # this is the funcion we call from main.py, it will call all the other funcion
    def run_game(self):
        self.intro()
        self.choose_mode()
        self.play_rounds()
        self.declare_winner()

    def intro(self):
        pass
    
    def choose_mode(self):
        user_choice = input("Press 1 for single player or 2 for multi-player: ")
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
    
    def play_rounds(self):
        while self.player_one.wins > 0 and self.player_two.wins > 0:
            self.player_one.choose_gesture
            print(f"{self.player_one} has chosen {self.player_one.chosen_gesture}")
            self.player_two.choose_gesture
            print(f"{self.player_two} has chosen {self.player_two.chosen_gesture}")
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print(f"It's a tie!")

    def declare_winner(self):
        pass