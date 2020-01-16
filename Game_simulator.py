
"""
Game Simulator
Started as an off-platform project for the CodeAcademy Python 3 course.
I've been adding to this project and improving it as I learn more about Python 3.

Planned improvements for the future:
Change error trapping for game_number so it allows for explansion of dictionaries offering new games
Error trap for running out of money - currently allows debt
Allow the game to be reset upon running out of money
Include a leader board
Remove maximum number of game plays when leader board is in place
Introduce a delay between each line of information appearing when the game is in play for added suspense!
"""


import games as f1

#This section contains dictionaries specifications for the games that can be played.

game_name_dict = {1: "flip a coin", 2: "cho han", 3: "pick a card", 4: "roulette"}
game_desc_dict = {1: "\nI will flip a coin.", 2: "\nI will roll two die and sum the values.", 3: "\nWe will each pick a card from the deck.", 4: "\nI will spin the roulette wheel."}
game_allowed_dict = {1: ["Heads", "Tails"], 2: ["Odd", "Even"], 3: ["Higher", "Lower"], 4: ["Odd", "Even", "Red", "Black", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "00"]} 
game_call_dict = {1: f1.game_1, 2: f1.game_2, 3: f1.game_3, 4: f1.game_4}

# This section sets the initial value for the variable money
money = 100

# This section welcomes the user to the Card Game Simulator and tells them about their starting money

print("Welcome to Card Game Simulator")
print("\nYou currently have £{} game money".format(str(money)))

# This section invites the user to choose which game to play, prints the results and updated the money variable.

# Allow the users to play games 10 times if they have money available
for i in range(1,10):
    print("\nWe have {} games available".format(len(game_name_dict)))
    for game_num, game_desc in game_name_dict.items():
        print("{} - {}".format(str(game_num), game_desc))
    game_number = input("\nEnter a number to play the game : ")
    if game_number not in ("1", "2", "3", "4"):
        print("Sorry, this is not a valid game number")
    else:
        money = f1.play_game(game_number, game_name_dict, game_desc_dict, game_allowed_dict, game_call_dict, money)
        i = i + 1
print("\nThank you for playing 10 games of Card Game Simulator.  We are trying to prevent our game becoming addictive.  Why not stop playing this game and make a nice cup of tea!")