import string
import random

letters = list(string.ascii_lowercase)

#letters_amount = len(letters)
#print(letters)
#print(letters_amount)

def letter_generator():
	print('This is an alphabet letter generator')
	print('To generate a letter press Y, to stop generator press N')

	prompt = input('\nGenerate a letter?')
	while True:
		if prompt == 'Y':
			rng = random.randint(0,25)
			print(letters[rng])
			prompt_2 = input('One more?')
		if prompt_2 == 'Y':
			print(letters[rng])
		elif prompt_2 == 'N':
			break

letter_generator()