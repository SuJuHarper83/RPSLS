from player import Player
import random
import time

class AI(Player):

    def __init__(self):
        self.name = "Luna"
        print("Luna has entered the game.")
        super().__init__()

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gesture_list)
        time.sleep(1)
        print(f'{self.name} has picked {self.chosen_gesture}')