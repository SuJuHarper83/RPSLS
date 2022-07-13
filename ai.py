from os import name
from player import Player
import random
import time

class AI(Player):

    def __init__(self):
        self.name = "Luna"
        print("Luna has entered the game.")
        time.sleep(1)
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        print(f"{self.name} has chosen {self.chosen_gesture}")
        time.sleep(1)