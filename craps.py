from random import randint

def craps(win):
	"""This function plays a craps game and returns whether or not it wins"""
	z = 0 # variable for later rolls
	a = randint(1, 6) + randint(1, 6) # come-out roll
	if a == 2:
		return win
	elif a == 3:
		return win
	elif a == 12:
		return win
	elif a == 7:
		return win + 1
	elif a == 11:
		return win + 1
	else:
		while z != a or z != 7:
			z = randint(1, 6) + randint(1, 6)
			if z == 7:
				return win
			elif z == a:
				return win + 1

def test(n):
	"""This allows the user to pick a number of craps games to play and
	returns the number of games won and what percentage were won (should
	be about .49%)"""
	win = 0
	for i in range(n):
		win = craps(win)
	win = win * 1.0
	n = n * 1.0
	odds = win/n
	print("You won", win, "games out of", n, "(", odds, "%).")

n = int(input("How many games do you want to play? "))
test(n)
