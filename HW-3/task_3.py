a = int(input("insert a: "))
b = int(input("insert b: "))
c = int(input("insert c: "))

#a, b
if a >= b and a > c and b > c or a > c and b >c:
	print("a + b = " + str(a + b))
#a, c
elif a > b and a >= c and c > b or a > b and c > b:
	print("a + c = " + str(a + c))
#b, c
elif b > a and b >= c and c > a or b > a and c > a:
	print("b + c = " + str(b + c))

else:
	print("Doesn't meet the condition of the task")