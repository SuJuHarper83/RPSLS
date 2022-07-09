class Player:

    def __init__(self):
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture = ""
        self.wins = 0

    def choose_gesture(self):
        print("Enter 0 to select Rock")
        print("Enter 1 to select Paper")
        print("Enter 2 to select Scissors")
        print("Enter 3 to select Lizard")
        print("Enter 5 to select Spock")
        user_choice = int(input("make your selection"))
        self.chosen_gesture = self.gesture_list[user_choice]
        