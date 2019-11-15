# import the randaom package so that we can generate a random choice
from random import randint 
from gameFunctions import winlose, config, comparison
# set up some variables for player and AI lives
# player_lives = 3
# jihee_lives = 3
# arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc
# choices is an array => an array is a container that can hold multiple values
# choices = ["rock","paper","scissors"]

# set the computer variable to one fo these choices
# jihee = choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time

while config.player is False:
	# set player to True
	print("*****************************\n\n")
	print("HELLO!! RPS WORLD!!\n\n")
	print("*****************************\n\n")
	print("jihee lives: ", config.jihee_lives, "/",config.total_lives,"\n")
	print("player lives: ", config.player_lives, "/",config.total_lives,"\n")
	print("Try to beat Jihee!\n\n")
	print("*****************************\n\n")

	config.player = input("choose rock, paper or scissors: ")
	config.player = config.player.lower()

	print("jihee chose ", config.jihee, "\n")
	print("player chose ", config.player, "\n")



	# player = input("choose rock, paper of scissors: ")
	# player = player.lower()

	# print("jihee chose",jihee,"\n")	
	# print("player chose",player,"\n")	

	comparison.compare()
	# if player.lower() == "quit":
	# 	exit()
	# elif jihee == player:
	# 	print("tie! no one wins, play agian")

	# elif player.lower() == "rock":
	# 	if jihee == "paper":
	# 		print("You lose!", jihee, "covers", player,"\n")
	# 		player_lives = player_lives - 1
	# 	else:
	# 		print("You win!", player, "smashes", jihee, "\n")
	# 		computer_lives = computer_lives - 1

	# elif player.lower()  == "paper":
	# 	if jihee == "scissors":
	# 		print("You lose!", jihee, "cuts", player,"\n")
	# 		player_lives = player_lives - 1
	# 	else:
	# 		print("You win!", player, "smashes", jihee, "\n")
	# 		jihee_lives = computer_lives - 1

	# elif player.lower()  == "scissors":
	# 	if jihee == "rock":
	# 		print("You lose!", jihee, "smashes", player,"\n")
	# 		player_lives = player_lives - 1
	# 	else:
	# 		print("You win!", player, "cuts", jihee, "\n")
	# 		jihee_lives = jihee_lives - 1

	# else:
	# 	print("That's not a valid choice, try agian")

	# handle all lives lost for player or AI
	if config.player_lives is 0:
		winlose.winorlose("lost")

	elif config.jihee_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		config.player = False
		config.jihee = config.choices[randint(0, 2)]	
