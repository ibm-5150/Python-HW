#1. Loop method

def factorial_n():
	n = int(input('Insert a number: '))
	factorial = 1
	for x in range(1, n+1):
		factorial = factorial * x
	print(f'Factorial of {n} is {factorial}')
factorial_n()

#2. Recursion method

def factorial_n(n):
	if n == 1:
		return 1
	else:
		return (n * factorial_n(n-1))
n = int(input('Insert a number: '))
print(f'Factorial of {n} is {factorial_n(n)}')







