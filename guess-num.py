import random

x = 0
y = input('Please enter the minimum value of the random number range!')
z = input('Please enter the maximuim value of the random number range!')
y = int(y)
z = int(z)
r = random.randint(y, z)
while True:
	guess = input('Guess a number!')
	guess = int(guess)
	x = x + 1
	if r == guess:
		print('Correct number!')
		print('You guessed', x,'times!')
		break
	elif r > guess:
		print('Too small!')
	elif r < guess:
		print('Too large!')
	print('You guessed', x,'times!')
