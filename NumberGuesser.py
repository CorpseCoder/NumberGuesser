import random
print("Welcome to my game!")
print("Ready to play?")
start = input("Enter Y for yes and N for no ")
if start == "Y":
	print("Select gamemode to play ")
	mode = input("Enter U for user defined limits and Enter C for computer defined limits ")
	if mode == "U":
		x = int(input("Enter the lower limit: "))
		y = int(input("Enter the higher limit: "))
		num = random.randint(x,y)
		turns = random.randint(1,10)
		while turns>0:
			guess = int(input("What's your guess? You have " + str(turns) + " guesses left "))
			if guess == num:
				print("Congrats, you found the number!")
				break
			else:
				print("That is not the correct number")
				turns=turns-1
	else:
		print("Gamemode coming soon...")
		exit()
else:
	exit()
