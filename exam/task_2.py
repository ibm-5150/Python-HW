import random
import string

def password_creator(pass_len):
	pass_chars = string.ascii_letters + string.digits
	password = ''.join((random.choice(pass_chars) for x in range(pass_len)))
	print(password)

password_creator(10)

