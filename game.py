# import the randaom package so that w ecan generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
choices = ["rock","paper","scissors"]

# set the computer variable to one fo these choices
computer = choices[randint(0,2)]

# set up the game loop so that we don't have to restart all the time
player = False

while player is False:
	# set player to True
	player = input("choose rock, paper of scissors\n")

	print("computer chose",computer,"\n")	
	print("player chose",player,"\n")	

	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play agian")

	# need to check all of our conditions after checking for a time
	player = False
	computer = choices [randint(0, 2)]
