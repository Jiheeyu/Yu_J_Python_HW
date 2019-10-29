# import the randaom package so that we can generate a random choice
from random import randint

# set up some variables for player and AI lives
player_lives = 5
computer_lives = 5
# arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc
# choices is an array => an array is a container that can hold multiple values
choices = ["rock","paper","scissors"]

# set the computer variable to one fo these choices
computer = choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player is False:
	# set player to True
	print("*****************************\n")
	print("Computer lives: ", computer_lives, "/5\n")
	print("player lives: ", player_lives, "/5\n")
	print("chose your weapon\n\n")
	print("*****************************\n")

	player = input("choose rock, paper of scissors: ")
	player = player.lower()

	print("computer chose",computer,"\n")	
	print("player chose",player,"\n")	

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play agian")

	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player,"\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower()  == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player,"\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

	elif player.lower()  == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player,"\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

	else:
		print("That's not a valid choice, try agian")

	# handle all lives lost for player or AI
	if player_lives is 0:
		print("out of lives! you suck at this game. WOuld you like to play agian?")
		choice = input("Y / N")
		print(choice)

		if (choice is "Y") or (choice is "n"):
			print("You chose to quit.")
			exit()
		elif (choice is "Y") or (choice is "y"):
			#reset the game so that we can start all over again
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choice[randint(0,2)]

	elif computer_lives is 0:
		print("Computer is out of lives! You rock at this game. WOuld you like to play agian?")
		choice = input("Y / N")
		print(choice)

		if (choice is "Y") or (choice is "n"):
			print("You chose to quit.")
			exit()
		elif (choice is "Y") or (choice is "y"):
			player_lives = 5
			computer_lives = 5
			player = False
			computer = choice[randint(0,2)]		

	else:
		# need to check all of our conditions after checking for a time
		player = False
		computer = choices[randint(0,2)]