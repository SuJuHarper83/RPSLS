from human import Human
from ai import AI
from player import Player

class Game:

    def __init__(self):
        self.player_one = Player
        self.player_two = Player

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
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print(f"It's a tie!")
        elif self.player_one == "Rock":
            if self.player_two == "Paper":
                print("Paper covers rock, you lose!")
                self.player_two.wins += 1
            elif self.player_two == "Scissors":
                print("Rock crushes scissors, you win!")
                self.player_one.wins +=1
            elif self.player_two == "Lizard":
                print("Rock crushes Lizard, you win!")
                self.player_one.wins += 1
            else:
                print("Try again")
        elif self.player_one == "Paper":
            if self.player_two == "Rock":
                print("Paper cobers rock, you win!")
                self.player_one.wins += 1
            elif self.player_two == "Scissors":
                print("Scissors cut paper, you lose!")
                self.player_two.wins +=1
            elif self.player_two == "Lizard":
                print("Lizard eats paper, you lose!")
                self.player_two.wins += 1
            else:
                print("Try again")
        elif self.player_one == "Lizard":
            if self.player_two == "Rock":
                print("Rock crushes lizard, you lose!")
                self.player_two.wins += 1
            elif self.player_two == "Scissors":
                print("Scissors decapitate lizard, you lose!")
                self.player_two.wins +=1
            elif self.player_two == "Paper":
                print("Lizard eats paper, you win!")
                self.player_one.wins += 1
            else:
                print("Lizard poisons Spoke, you win!")
                self.player_one.wins += 1
        elif self.player_one == "Scissors":
            if self.player_two == "Spock":
                print("Spock smashes scissors, you lose!")
                self.player_two.wins += 1
            elif self.player_two == "Paper":
                print("Scissors cut paper, you win!")
                self.player_one.wins +=1
            elif self.player_two == "Rock":
                print("Rock smashes scissors, you lose!")
                self.player_two.wins += 1
            else:
                print("Try again")
        elif self.player_one == "Spock":
            if self.player_two == "Scissors":
                print("Spock smashes scissors, you win!")
                self.player_one.wins += 1
            elif self.player_two == "Lizard":
                print("Lizard poisons Spock, you lose!")
                self.player_two.wins +=1
            else:
                print("Try again")

    def declare_winner(self):
        pass