import random

print("Guess a number 1999 - 2020. All rights reserved")
print("\n-----------------------------------------------")

user_name = input("\nInsert your name: ")

number = random.randint(1,10)

print(f"\n{user_name}, you have 3 tries to guess a number from 1 to 10")

try_1 = int(input(">>> Insert a number: "))

if try_1 == number:
	print("\n--------")
	print("You win!")
	print("--------")
elif try_1 > number:
	print(f"\nNumber is less than {try_1}")
elif try_1 < number:
	print(f"\nNumber is greater than {try_1}")

try_2 = int(input(">>> Insert a number: "))

if try_2 == number:
	print("\n--------")
	print("You win!")
	print("--------")
elif try_2 > number:
	print(f"\nNumber is less than {try_2}")
elif try_2 < number:
	print(f"\nNumber is greater than {try_2}")

try_3 = int(input(">>> Insert a number: "))

if try_3 == number:
	print("\n--------")
	print("You win!")
	print("--------")
elif try_3 > number:
	print(f"\nNumber is less than {try_3}")
elif try_3 < number:
	print(f"\nNumber is greater than {try_3}")

if try_1 != number and try_2 != number and try_3 != number:
	print(f"\nYou lose! Better luck next time, {user_name}")

print("\n-----------------------------------------------")
