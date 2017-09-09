from random import randint

def play(wallet = 50):
	"""This function plays a craps game while allowing you to bet."""
	while wallet > 0:
		print ("You have", wallet, "to bet.")
		bet = (int(input("Please enter your wager (in an integer): ")))
		if bet.isdigit() == False:
			bet = (int(input("I said an integer! Try again: ")))
		while bet > wallet:
			bet = (int(input("You don't have that much money! Try again: ")))
		z = 0 # variable for later rolls
		a = randint(1, 6) + randint(1, 6) # come-out roll
		if a == 2:
			wallet -= bet
			print("Snake eyes! You lose. You have", wallet, "remaining.")
			retry = input("Try again? Y/N: ")
			if retry[0].lower() == "y":
				play(wallet)
			elif retry[0].lower() == "n":
				print("OK. Goodbye!")
				quit()
			else:
				retry = input("Please enter Y or N. Try again? Y/N: ")
		elif a == 3:
			wallet -= bet
			print("3! You lose. You have", wallet, "remaining. ")
			retry = input("Try again? Y/N: ")
			if retry[0].lower() == "y":
				play(wallet)
			elif retry[0].lower() == "n":
				print("OK. Goodbye!")
				quit()
			else:
				retry = input("Please enter Y or N. Try again? Y/N: ")
		elif a == 12:
			wallet -= bet
			print("Boxcars! You lose. You have", wallet, "remaining.")
			retry = input("Try again? Y/N: ")
			if retry[0].lower() == "y":
				play(wallet)
			elif retry[0].lower() == "n":
				print("OK. Goodbye!")
				quit()
			else:
				retry = input("Please enter Y or N. Try again? Y/N: ")
		elif a == 7:
			wallet += bet
			print("7, lucky winner! You have", wallet, "remaining.")
			retry = input("Try again? Y/N: ")
			while retry:
				if retry[0].lower() == "y":
					play(wallet)
				elif retry[0].lower() == "n":
					print("OK. Goodbye!")
					quit()
				else:
					retry = input("Please enter Y or N. Try again? Y/N: ")
		elif a == 11:
			wallet += bet
			print("11, lucky winner! You have", wallet, "remaining.")
			retry = input("Try again? Y/N: ")
			while retry:
				if retry[0].lower() == "y":
					play(wallet)
				elif retry[0].lower() == "n":
					print("OK. Goodbye!")
					quit()
				else:
					retry = input("Please enter Y or N. Try again? Y/N: ")
		else:
			print("You rolled:", a)
			while z != a or z != 7:
				z = randint(1, 6) + randint(1, 6)
				if z == 7:
					wallet -= bet
					print("Uhoh, 7! You lose. You have", wallet, "remaining.")
					retry = input("Try again? Y/N: ")
					if retry[0].lower() == "y":
						play(wallet)
					elif retry[0].lower() == "n":
						print("OK. Goodbye!")
						quit()
				elif z == a:
					wallet += bet
					print(a, "lucky winner! You have", wallet, "remaining.")
					retry = input("Try again? Y/N: ")
					while retry:
						if retry[0].lower() == "y":
							play(wallet)
						elif retry[0].lower() == "n":
							print("OK. Goodbye!")
							quit()
						else:
							retry = input("Please enter Y or N. Try again? Y/N: ")
				else:
					print("You rolled:", z)
		print("Uhoh, you're out of money! Better luck next time.")
		quit()

play(50)
