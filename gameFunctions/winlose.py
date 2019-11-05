from random import randint
#define a python function that takes an argument
def winorlose(status):
	#status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("************************")

	print("You", status, "! Would you like to play agian?")

	choice = input("Y / N")
	print(choice)

	if (choice is "Y") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so that we can start all over again
		global player_lives
		global computer_lives
		global player
		global computer
		global choices

		player_lives = 1
		computer_lives = 1
		player = False
		computer = choice[randint(0,2)]
