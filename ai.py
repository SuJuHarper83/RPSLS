from player import Player
import random

class AI(Player):

    def __init__(self):
        self.name = "Luna"
        print("Luna has entered the game.")
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        print(f'{self.name} has picked {self.chosen_gesture}')