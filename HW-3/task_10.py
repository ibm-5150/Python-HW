fib = int(input("Members of Fibonacci sequence: "))

a = 0
b = 1

print(b)
print(b)

for x in range(2, fib + 1):
	
	c = a + b
	a = b
	b = c

	print(a + b)