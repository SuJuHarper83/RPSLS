from player import Player

class Human(Player):

    def __init__(self):
        self.name = input("What is your name? ")
        print(f"Welcome {self.name}!")
        super().__init__()

    def choose_gesture(self):
        print("Enter 0 to select Rock")
        print("Enter 1 to select Paper")
        print("Enter 2 to select Scissors")
        print("Enter 3 to select Lizard")
        print("Enter 4 to select Spock")
        user_choice = int(input("make your selection: "))
        self.chosen_gesture = self.gesture_list[user_choice]
        print(f"{self.name} has chosen {self.chosen_gesture}")