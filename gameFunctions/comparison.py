from random import randint
from gameFunctions import config

def compare():
	player = input("choose rock, paper of scissors: ")
	player = player.lower()
	choices = ["rock","paper","scissors"]
	jihee = choices[randint(0,2)]

	print("jihee chose",jihee,"\n")	
	print("player chose",player,"\n")	


	if player.lower() == "quit":
			exit()

	elif jihee == player:
			print("tie! no one wins, play agian")

	elif player.lower() == "rock":
		if jihee == "paper":
			print("You lose!", jihee, "covers", player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", player, "smashes", jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	elif player.lower()  == "paper":
		if jihee == "scissors":
			print("You lose!", jihee, "cuts", player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", player, "smashes", jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	elif player.lower()  == "scissors":
		if jihee == "rock":
			print("You lose!", jihee, "smashes", player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", player, "cuts", jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	else:
		print("That's not a valid choice, try again")
