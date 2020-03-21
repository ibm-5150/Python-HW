import math

a = float(input())
b = float(input())
c = float(input())

D = b**2-4*a*c

if D < 0: 
	print("no roots")
elif D == 0:
	print("1 root")
elif D > 0:
	print("2 roots")

x1 = (-b+math.sqrt(D))/2*a
x2 = (-b-math.sqrt(D))/2*a

print("x1= " + str(x1)+ "x2= "+str(x2))