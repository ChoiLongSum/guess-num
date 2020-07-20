import random

r = random.randint(1, 100)
x = 0
while True:
	guess = input('guess a number from 1-100!')
	guess = int(guess)
	x = x + 1
	if r == guess:
		print('Correct number!')
		print('you guessed', x,'times!')
		break
	elif r > guess:
		print('Too small!')
	elif r < guess:
		print('too large!')
	print('you guessed', x,'times!')
