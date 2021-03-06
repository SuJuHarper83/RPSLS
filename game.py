from human import Human
from ai import AI
from player import Player
import time

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
        time.sleep(1)
        print("Let's have a rock, paper, scissors game, Big Bang Theory style!")
        time.sleep(1)
    
    def choose_mode(self):
        user_choice = input("Press 1 for single player or 2 for multi-player: ")
        if user_choice == "1":
            self.player_one = Human()
            self.player_two = AI()
        elif user_choice == "2":
            self.player_one = Human()
            self.player_two = Human()
    
    def play_rounds(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print(f"It's a tie!")
                time.sleep(1)
            elif self.player_one.chosen_gesture == "Rock":
                if self.player_two.chosen_gesture == "Paper":
                    print(f"Paper covers rock, {self.player_two.name} wins!")
                    time.sleep(1)
                    self.player_two.wins += 1
                elif self.player_two.chosen_gesture == "Scissors":
                    print("Rock crushes scissors, you win!")
                    self.player_one.wins +=1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Lizard":
                    print("Rock crushes Lizard, you win!")
                    self.player_one.wins += 1
                    time.sleep(1)
                else:
                    print("Try again")
                    time.sleep(1)
            elif self.player_one.chosen_gesture == "Paper":
                if self.player_two.chosen_gesture == "Rock":
                    print("Paper cobers rock, you win!")
                    self.player_one.wins += 1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Scissors":
                    print(f"Scissors cut paper, {self.player_two.name} wins!")
                    self.player_two.wins +=1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Lizard eats paper, {self.player_two.name} wins!")
                    self.player_two.wins += 1
                    time.sleep(1)
                else:
                    print("Try again")
            elif self.player_one.chosen_gesture == "Lizard":
                if self.player_two.chosen_gesture == "Rock":
                    print(f"Rock crushes lizard, {self.player_two.name} wins!")
                    self.player_two.wins += 1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Scissors":
                    print(f"Scissors decapitate lizard, {self.player_two.name} wins!")
                    self.player_two.wins +=1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Paper":
                    print("Lizard eats paper, you win!")
                    self.player_one.wins += 1
                    time.sleep(1)
                else:
                    print("Lizard poisons Spock, you win!")
                    self.player_one.wins += 1
                    time.sleep(1)
            elif self.player_one.chosen_gesture == "Scissors":
                if self.player_two.chosen_gesture == "Spock":
                    print(f"Spock smashes scissors, {self.player_two.name} wins!")
                    self.player_two.wins += 1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Paper":
                    print("Scissors cut paper, you win!")
                    self.player_one.wins +=1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Rock":
                    print(f"Rock smashes scissors, {self.player_two.name} wins!")
                    self.player_two.wins += 1
                    time.sleep(1)
                else:
                    print("Try again")
                    time.sleep(1)
            elif self.player_one.chosen_gesture == "Spock":
                if self.player_two.chosen_gesture == "Lizard":
                    print("Spock smashes scissors, you win!")
                    self.player_one.wins += 1
                    time.sleep(1)
                elif self.player_two.chosen_gesture == "Lizard":
                    print(f"Lizard poisons Spock, {self.player_two.name} wins!")
                    self.player_two.wins +=1
                    time.sleep(1)
                else:
                    print("Try again")
                    time.sleep(1)

    def declare_winner(self):
        if self.player_one.wins == 2:
            print(f"You win 2 out of 3!")
            time.sleep(1)
        elif self.player_two.wins == 2:
            print(f"{self.player_two.name} wins 2 out of 3!")
            time.sleep(1)