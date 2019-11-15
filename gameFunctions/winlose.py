from random import randint
from gameFunctions import config

#define a python function that takes an argument
def winorlose(status):
	#status will be either won or lost - you're passing this in as an argument
	print("************************")
	print("called win or lose")
	print("************************")

	print("You", status + "! Would you like to play agian?")

	choice = input("Y / N")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so that we can start all over again

		config.player_lives = 5
		config.jihee_lives = 5
		config.player = False
		config.jihee = config.choices[randint(0,2)]

	else:
		print("That's not a valid choice, try again")
		winorlose(status)

