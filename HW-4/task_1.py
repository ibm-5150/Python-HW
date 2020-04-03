import random

print("               GUESS A NUMBER                  ")
print("\n-----------------------------------------------")

user_name = input("\nInsert your name: ")

number = random.randint(1,10)

print(f"\n{user_name}, you have 3 tries to guess a number from 1 to 10")

tries = 0

while tries < 3:
	try_num = int(input(">>> Insert a number: "))
	if try_num == number:
		print("\n--------")
		print("You win!")
		print("--------")
		break
	elif try_num > number:
		tries = tries + 1
		print(f"Number is less than {try_num}")
	elif try_num < number:
		tries = tries + 1
		print(f"Number is greater than {try_num}")
#Summary
if try_num != number:
	print(f"\nYou lose! Better luck next time, {user_name}")

print("\n-----------------------------------------------")
