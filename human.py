from player import Player

class Human(Player):

    def __init__(self):
        self.name = input("What is your name? ")
        print(f"Welcome {self.name}!")
        super().__init__()