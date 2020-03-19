import math

t1 = float(input())
g1 = float(input())
t2 = float(input())
g2 = float(input())

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2	))

#https://kite.com/python/answers/how-to-print-the-degree-symbol-in-python 
d = u"\N{DEGREE SIGN}"

r = round(distance)

print("t1= " + str(t1)+str(d))
print("g1= " + str(g1)+str(d))
print("t2= " + str(t2)+str(d))
print("g2= " + str(g2)+str(d))

print("The distance between these points is: " + str(r) + "km")
