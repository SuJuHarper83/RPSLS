from re import A
from player import Player
import time

class Human(Player):

    def __init__(self):
        self.name = input("What is your name? ")
        time.sleep(1)
        print(f"Welcome {self.name}!")
        time.sleep(1)
        super().__init__()

    def choose_gesture(self):
        print("Enter 0 to select Rock")
        time.sleep(1)
        print("Enter 1 to select Paper")
        time.sleep(1)
        print("Enter 2 to select Scissors")
        time.sleep(1)
        print("Enter 3 to select Lizard")
        time.sleep(1)
        print("Enter 4 to select Spock")
        time.sleep(1)
        user_choice = int(input("make your selection: "))
        self.chosen_gesture = self.gesture_list[user_choice]
        time.sleep(1)
        print(f"{self.name} has chosen {self.chosen_gesture}")