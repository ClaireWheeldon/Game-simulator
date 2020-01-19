# This file contains the functions for the game simulator.

import random

# this function inititalises the games menu and allows the user to choose a game
def games_menu():
	print("\nWelcome to Card Game Simulator")

	# set initial value of money as £100
	money = 100

	#Set dictionary specifications for the games that can be played
	game_name_dict = {1: "flip a coin", 2: "cho han", 3: "pick a card", 4: "roulette"}
	game_desc_dict = {1: "\nI will flip a coin.", 2: "\nI will roll two die and sum the values.", 3: "\nWe will each pick a card from the deck.  Predict if your card will be higher or lower than mine.", 4: "\nI will spin the roulette wheel."}
	game_predict_desc_dict = {1: "heads or tails", 2: "odd or even", 3: "higher or lower", 4: "odd or even, red or black, 0 to 36 or 00"}
	game_predict_value_dict = {1: ["heads", "tails"], 2: ["odd", "even"], 3: ["higher", "lower"], 4: ["odd", "even", "red", "black", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "00"]} 
	game_call_dict = {1: game_1, 2: game_2, 3: game_3, 4: game_4}

	# invite the user to play games 
	first_time = True
	while money > 0:
		if first_time:
			print("\nWe have {} games available".format(len(game_name_dict)))
		else:
			new_game = validate_input_allowed_list("\nWould you like to play again? Enter Y or N :", ["Y", "N"])
			if new_game == "N":
				print("Goodbye, thanks for playing")
			else:
				print("\nLet's play again!")
		for game_num, game_desc in game_name_dict.items():
			print("{} - {}".format(str(game_num), game_desc))
		game_number = validate_input_allowed_list("\nEnter a number to play the game : ", ["1", "2", "3", "4"])
		first_time = False
		money = play_game(game_number, game_name_dict, game_desc_dict, game_predict_desc_dict, game_predict_value_dict, game_call_dict, money)
	print("\nGAME OVER - you have run out of money")
	again = validate_input_allowed_list("\nWould you like to play again? Enter Y or N :", ["Y", "N"])
	if again == "Y":
		money = 100
		games_menu()
	else:
		print("\nThanks for playing, goodbye.")

# This function creates an input box and validates the value entered 
# user input must be in the list of allowed values
# returns the validated input
def validate_input_allowed_list(prompt_message, allowed_values):
	user_value = input(prompt_message)
	user_value_lc = user_value.lower()
	if user_value_lc in allowed_values:
		return user_value
	else:
		print("Sorry this is not an option.")
		return validate_input_allowed_list(prompt_message, allowed_values)

# This function creates an input box and validates the value entered 
# user input must be able to be converted to an integer
# user input must be greater than minimum_value
# user input must be less than or equal to maximum_value
# returns the validated input
def validate_input_range(prompt_message, minimum_value, maximum_value):
	user_value = input(prompt_message)
	try:
		user_value_int = int(user_value)
		if user_value_int > minimum_value and user_value_int <= maximum_value:
			return user_value_int
		else:
			print("Sorry, your bet needs to be between {} and {}".format(minimum_value, maximum_value))
			return validate_input_range(prompt_message, minimum_value, maximum_value)
	except:
		print("Sorry, please enter a whole number.")
		return validate_input_range(prompt_message, minimum_value, maximum_value)

""" This function describes the game to the user.
 It asks them to predict the outcome with error checking on their input.  
 It allows them to place a bet on the game with error checking on their input.
 It then calls the relevant game function to run the game"""
def play_game(game_number, game_name_dict, game_desc_dict, game_predict_desc_dict, game_predict_value_dict, game_call_dict, money):
	game_integer = int(game_number)
	print(game_desc_dict[game_integer])
	# ask user to predict the outcome of the game
	predict_values = game_predict_value_dict[game_integer]
	predict_message = "Enter your prediction, {} :".format(game_predict_desc_dict[game_integer])
	predict = validate_input_allowed_list(predict_message, predict_values)
	# ask user for their bet
	print("\nYou currently have £{} game money".format(str(money)))
	bet_message = "How much do you want to bet? Please enter as an integer £"
	bet_minimum = 0
	bet_maximum = money
	bet_type = "int"
	bet = validate_input_range(bet_message, bet_minimum, bet_maximum)
	# Play the game by calling the appropriate game function e.g. game_1 for Flip Coin
	game_variables = game_call_dict[game_integer](bet, predict, money)
	money, message = game_variables
	print(message)
	return money
	
"""Code Academy specification for this function:
Create a function that simulates flipping a coin and calling either "Heads" or "Tails". 
This function (along with all of the other functions you will write in this project) should have a parameter that represents 
how much the player is betting on the coin flip.
This function should also have a parameter that lets the player call either "Heads" or "Tails".
If the player wins the game, the function should return the amount that they won. 
If the player loses the game, the function should return the amount that they lost as a negative number."""
def game_1(bet, predict, money):
	message = "\nYou played flip a coin.\n"
	num = random.randint(1, 2)
	if num == 1:
		message += "The coin landed on heads.\n"
		if predict == "heads":
			message += "You won £{}.\n".format(str(bet * 2))
			money = money + (bet * 2)
		else:
			message += "You lost £{}.\n".format(str(bet))
			money = money + (bet * -1)
	else:
		message += "The coin landed on tails.\n" 
		if predict == "tails":
			message += "You won £{}.\n".format(str(bet * 2))
			money = money + (bet * 2)
		else:
			message += "You lost £{}.\n".format(str(bet))
			money = money + (bet * -1)
	message += "Your game money is now £{}.".format(str(money))
	game_variables = (money, message)
	return game_variables

"""Create a function that simulates playing the game Cho-Han. The function should simulate rolling two dice and adding the results together.
The player predicts whether the sum of those dice is odd or even and wins if their prediction is correct.
The function should have a parameter that allows for the player to guess whether the sum of the two dice is "Odd" or "Even". 
The function should also have a parameter that allows the player to bet an amount of money on the game."""

def game_2(bet, predict, money):
	message = "\nYou played cho han.\n"
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	sum_die = dice1 + dice2
	message += "Dice 1 rolled a {}\n".format(str(dice1))
	message += "Dice 2 rolled a {}\n".format(str(dice2))
	message += "The sum of the two dice is {}\n".format(str(sum_die))
	if sum_die % 2 == 0 and predict == "even":
		message += "The sum of the two dice was even.\n"
		message += "You won £{}.\n".format(str(bet * 2))
		money = money + (bet * 2)
	elif sum_die % 2 != 0 and predict == "odd":
		message += "The sum of the two dice was odd.\n"
		message += "You won £{}.\n".format(str(bet * 2))
		money = money + (bet * 2)
	else:
		message += "The sum of the two dice was not {}.\n".format(predict)
		message += "You lost £{}.\n".format(str(bet))
		money = money + (bet * -1)
	message += "Your game money is now £{}.".format(str(money))
	game_variables = (money, message)
	return game_variables

""" Create a function that simulates two players picking a card randomly from a deck of cards. 
The higher number wins.
Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. 
In this game, there can be a tie. 
What should be returned if there is a tie?
Check the hint to see an additional challenge for this game. """

def game_3(bet, predict, money):
	message = "\nYou played pick a card.\n"
	suit_dict = {1: "Hearts", 2: "Diamonds", 3: "Spades", 4: "Clubs"}
	card_dict = {2: "a Two", 3: "a Three", 4: "a Four", 5: "a Five", 6: "a Six", 7: "a Seven", 8: "an Eight", 9: "a Nine", 10: "a Ten", 11: "a Jack", 12: "a Queen", 13: "a King", 14: "an Ace"}
	pack1_card_value = random.randint(2,12)
	pack1_card_name = card_dict[pack1_card_value]
	pack1_suit_value = random.randint(1,4)
	pack1_suit_name = suit_dict[pack1_suit_value]
	pack2_card_value = random.randint(2,14)
	pack2_card_name = card_dict[pack2_card_value]
	pack2_suit_value = random.randint(1,4)
	pack2_suit_name = suit_dict[pack2_suit_value]
	message += "Your card is {} of {}.\n".format(str(pack1_card_name), str(pack1_suit_name))
	message += "My card is {} of {}.\n".format(str(pack2_card_name), str(pack2_suit_name))
	if predict == "higher":
		if pack1_card_value > pack2_card_value:
			message += "Your card is the highest. \n"
			outcome = "won"
			bet_multiplier = 2
		elif pack1_card_value == pack2_card_value:
			message += "Your card is the same value as mine.\n"
			outcome = "neither"
			bet_multiplier = 1
		else:
			message += "Your card is not the highest.\n"	
			outcome = "lost"
			bet_multiplier = -1
	elif predict == "lower":
		if pack1_card_value < pack2_card_value:
			message += "Your card is the lowest. \n"
			outcome = "won"
			bet_multiplier = 2
		elif pack1_card_value == pack2_card_value:
			message += "Your card is the same value as mine.\n"
			outcome = "neither won nor lost"
			bet_multiplier = 1
		else:
			message += "Your card is not the lowest.\n"	
			outcome = "lost"
			bet_multiplier = -1

	message += "You {} £{}\n".format(outcome, str(abs(bet * bet_multiplier)))
	money = money + (bet * bet_multiplier)		
	
	message += "Your game money is now £{}.".format(str(money))
	game_variables = (money, message)
	return game_variables

"""Create a function that simulates some of the rules of roulette. 
A random number should be generated that determines which space the ball lands on.
When we wrote our function, we allowed the user to guess "Odd", "Even", or a specific number. 
We also implemented the logic associated with the 0 and 00 spots. 
For example, the player loses if they guess either "Odd" or "Even" and either 0 or 00 comes up.
Implement as many rules of roulette as you’d like. 
Make sure to consider the different ways roulette rewards a win. 
Check the hint to see more about this!"""

def game_4(bet, predict, money):
	message = "\nYou played roulette.\n"
	spin = random.randint(1,38)

# convert predict of 0 or 00 to 37 or 38
	if predict == "0":
		predict = "37"
	elif predict == "00":
		predict = "38"
	
	# calculate whether the spin is even or odd.  
	# 37 represents 0 and 38 represents 00
	if spin == 37 or spin == 38:
		spin_type = "neither odd nor even"
	elif (spin % 2) == 0: 
		spin_type = "even"
	else:
		spin_type = "odd"

	# calculate whether the spin is red or black.  
	# 37 represents 0 and 38 represents 00
	red_numbers = [1, 36, 3, 34, 5, 32, 7, 30, 9, 14, 23, 16, 21, 18, 19, 12, 25, 27]
	if spin == 37 or spin == 38:
		spin_colour = "green"
	elif spin in red_numbers:
		spin_colour = "red"
	else:
		spin_colour = "black"

	#display what number the wheel landed on
	if spin == 37:
		spin_name = "0"
	elif spin == 38:
		spin_name = "00"
	else:
		spin_name = spin
	message += "The number on the wheel was {}.\n".format(str(spin_name))

	#for predict = Odd or Even, calculate if there is a win
	if predict == "odd" or predict == "even":
		message += "The number on the wheel was {}.\n".format(spin_type)
		if (predict == "odd" and spin_type == "odd") or (predict == "even" and spin_type == "even"):
			outcome = "won"
			bet_multiplier = 2
		else:
			outcome = "lost"
			bet_multiplier = -1
	#for predict = Red or Black, calculate if there is a win 
	elif predict == "red" or predict == "black":
		message += "The number on the wheel was {}.\n".format(spin_colour)
		if (predict == "red" and spin_colour == "red") or (predict == "black" and spin_colour == "black"):
			outcome = "won"
			bet_multiplier = 2
		else:
			outcome = "lost"
			bet_multiplier = -1
	#for predict = a single number, calculate if there is a win 
	else:	
		if int(predict) == spin:
			outcome = "won"
			bet_multiplier = 10
		else:
			outcome = "lost"
			bet_multiplier = -1	
	money = money + (bet * bet_multiplier)
	message += "You {} £{}.\n".format(outcome, str(abs(bet * bet_multiplier)))
	message += "Your game money is now £{}.".format(str(money))
	game_variables = (money, message)
	return game_variables