def prime_number(num):
	if num>1 and num%num == 0 and num%2 !=0:
		print(f'{num} is prime')
	else:
		print(f'{num} is complex')

prime_number(5)