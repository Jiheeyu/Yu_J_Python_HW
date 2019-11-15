from gameFunctions import config

def compare():
	if config.player.lower() == "quit":
			exit()
	elif config.jihee == config.player:
			print("tie! no one wins, play agian")

	elif config.player.lower() == "rock":
		if config.jihee == "paper":
			print("You lose!", config.jihee, "covers", config.player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", config.player, "smashes", config.jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	elif config.player.lower()  == "paper":
		if config.jihee == "scissors":
			print("You lose!", config.jihee, "cuts", config.player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", config.player, "smashes", config.jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	elif config.player.lower()  == "scissors":
		if config.jihee == "rock":
			print("You lose!", config.jihee, "smashes", config.player,"\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", config.player, "cuts", config.jihee, "\n")
			config.jihee_lives = config.jihee_lives - 1

	else:
		print("That's not a valid choice, try again")
