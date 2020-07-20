import random

r = random.randint(1, 100)

while True:
	guess = input('guess a number from 1-100!')
	guess = int(guess)
	if r == guess:
		print('Correct number!')
		break
	elif r > guess:
		print('Too small!')
	elif r < guess:
		print('too large!')
