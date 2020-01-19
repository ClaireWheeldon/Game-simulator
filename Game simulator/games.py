# This file contains the functions for the game simulator.

import random

money = 100

# This function allows the user to select which game to play.  
# It then describes the game to the user.
# It asks them to predict the outcome with error checking on their input.  
# It allows them to place a bet on the game with error checking on their input.
# It then calls the relevant game function to run the game

def play_game(game_number, game_name_dict, game_desc_dict, game_allowed_dict, game_call_dict, money):
	game_integer = int(game_number)
	# Describe game to user
	print(game_desc_dict[game_integer])
	# Create variable allowed_values to contain all allowed values for predict for this game
	allowed_values = game_allowed_dict[game_integer]
	# Create a string describing the allowed values for predict
	allowed_str = ""
	for allowed in allowed_values:
		allowed_str += allowed + " or "
	allowed_str = allowed_str[0:-3]
	# Ask user for a predicted value from the list of allowed values
	predict = input("\nEnter your prediction, {}:".format(allowed_str))
	# Validate the users input for predict and communicate about their prediction.
	predict_message, valid_predict, predict = check_predict(predict, game_allowed_dict[game_integer])
	print(predict_message)
	# Tell user how much game money they have
	print("\nYou currently have £{} game money".format(str(money)))
	# If predict is valid ask user for their bet
	if valid_predict:
		valid_bet = False
		while valid_bet == False:
			bet = input("How much do you want to bet? Please enter as an integer £")
			# Validate the users input for bet and communicate about their prediction.
			bet_message, valid_bet, bet = check_bet(bet, money)
			print(bet_message)
		# If bet is valid then play the game	
		# call the appropriate game function e.g. game_1 for Flip Coin
		game_variables = game_call_dict[game_integer](bet, predict, money)
		money, message = game_variables
		print(message)
	return money
	
# This is an error trapping function for checking the validity of the user input bet
# bet must be able to be converted to an game_integer
# bet must be less than money
# bet must be greater than 0


def check_bet(bet, money):
	# test that bet is an integer
	try: 
		int_bet = int(bet)
		# test that bet < money
		if int_bet > money:
			bet_message = "Sorry, you do not have enough money."
			valid_bet = False
		#test that bet > 0
		elif int_bet <= 0:
			bet_message = "Sorry, bets must be greater than zero."
			valid_bet = False
		else:
			bet_message = ""
			valid_bet = True
	except:
		bet_message = "Sorry, please enter a whole number."
		valid_bet = False
		int_bet = 0

	return bet_message, valid_bet, int_bet

# This is an error trapping funtion for checking the validity of the user input predict
# predict can only take the value good1 of good2.

def check_predict(predict, allowed_values):
	predict_lc = predict.lower()
	predict_message = ""
	if predict_lc in allowed_values:
		valid_predict = True
		predict_message += "You predicted {}.".format(predict)
	else:
		valid_predict = False
		predict_message += "\nSorry, this is not a valid prediction."
	return predict_message, valid_predict, predict_lc

"""Code Academy specification for this function:
Create a function that simulates flipping a coin and calling either "Heads" or "Tails". 
This function (along with all of the other functions you will write in this project) should have a parameter that represents 
how much the player is betting on the coin flip.
This function should also have a parameter that lets the player call either "Heads" or "Tails".
If the player wins the game, the function should return the amount that they won. 
If the player loses the game, the function should return the amount that they lost as a negative number."""

def game_1(bet, predict, money):
	message = "You played Flip Coin.\n"
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
	message = "You played Cho Han.\n"
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
	message = "You played Pick a Card.\n"
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
	message = "You played Roulette.\n"
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