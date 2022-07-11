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
        self.declare_winner(self)

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
        while True:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print(f"It's a tie!")
            elif self.player_one.chosen_gesture == "Rock":
                if self.player_two.chosen_gesture == "Paper":
                    print("Paper covers rock, Luna wins!")
                    self.player_two.wins += 1
                elif self.player_two.chosen_gesture == "Scissors":
                    print("Rock crushes scissors, you win!")
                    self.player_one.wins +=1
                elif self.player_two.chosen_gesture == "Lizard":
                    print("Rock crushes Lizard, you win!")
                    self.player_one.wins += 1
                else:
                    print("Try again")
            elif self.player_one.chosen_gesture == "Paper":
                if self.player_two.chosen_gesture == "Rock":
                    print("Paper cobers rock, you win!")
                    self.player_one.wins += 1
                elif self.player_two.chosen_gesture == "Scissors":
                    print("Scissors cut paper, Luna wins!")
                    self.player_two.wins +=1
                elif self.player_two.chosen_gesture == "Lizard":
                    print("Lizard eats paper, Luna wins!")
                    self.player_two.wins += 1
                else:
                    print("Try again")
            elif self.player_one.chosen_gesture == "Lizard":
                if self.player_two.chosen_gesture == "Rock":
                    print("Rock crushes lizard, Luna wins!")
                    self.player_two.wins += 1
                elif self.player_two.chosen_gesture == "Scissors":
                    print("Scissors decapitate lizard, Luna wins!")
                    self.player_two.wins +=1
                elif self.player_two.chosen_gesture == "Paper":
                    print("Lizard eats paper, you win!")
                    self.player_one.wins += 1
                else:
                    print("Lizard poisons Spock, you win!")
                    self.player_one.wins += 1
            elif self.player_one.chosen_gesture == "Scissors":
                if self.player_two.chosen_gesture == "Spock":
                    print("Spock smashes scissors, Luna wins!")
                    self.player_two.wins += 1
                elif self.player_two.chosen_gesture == "Paper":
                    print("Scissors cut paper, you win!")
                    self.player_one.wins +=1
                elif self.player_two.chosen_gesture == "Rock":
                    print("Rock smashes scissors, Luna wins!")
                    self.player_two.wins += 1
                else:
                    print("Try again")
            elif self.player_one.chosen_gesture == "Spock":
                if self.player_two.chosen_gesture == "Lizard":
                    print("Spock smashes scissors, you win!")
                    self.player_one.wins += 1
                elif self.player_two.chosen_gesture == "Lizard":
                    print("Lizard poisons Spock, Luna wins!")
                    self.player_two.wins +=1
                else:
                    print("Try again")

    def declare_winner(self):
        if self.player_one.wins <= 3:
            print(f"{self.player_one.name} wins!")
        elif self.player_two.wins <= 3:
            print(f"{self.player_two.name} wins!")