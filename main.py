# create RPSLS game
# As a developer, I want to make at least 10 commits with descriptive messages. 
# As a developer, I want to find a way to properly incorporate inheritance into my game.  
# As a developer, I want to account for and handle bad user input, 
# ensuring that any user input is validated and reobtained if necessary.  
# As a developer, I want to store all of the gesture options/choices in a list. 
# I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc). 
# As a player, I want the correct player to win a given round based on the choices made by each player.  
# As a player, I want the game of RPSLS to be at minimum a “best of three” to decide a winner.  
# As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs human) game. 


# Introduction
# Rules of the game
# prestent user game mode options
# Create players: 
#   ai, human
# Create attack phase while loop
# Display winner best out of 3

# Classes:
#   Player will be our parent class
#   Human player #input
#   AI player #random11
#   Game #holds the choices

from game import Game

game_one = Game()
game_one.run_game()
