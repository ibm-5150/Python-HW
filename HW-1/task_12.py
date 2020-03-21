import math

t1 = float(input())
g1 = float(input())
t2 = float(input())
g2 = float(input())

#pi=22/7
#radian = degree*(pi/180)
#https://www.w3resource.com/python-exercises/math/python-math-exercise-1.php


x1 = math.radians(t1)
y1 = math.radians(g1)
x2 = math.radians(t2)
y2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2	))

#https://kite.com/python/answers/how-to-print-the-degree-symbol-in-python 
d = u"\N{DEGREE SIGN}"

r = round(distance)

print("t1= " + str(t1)+str(d) + "    t1= " + str(x1) + "rad")
print("g1= " + str(g1)+str(d) + "    g1= " + str(x1) + "rad")
print("t2= " + str(t2)+str(d) + "    t2= " + str(x1) + "rad")
print("g2= " + str(g2)+str(d) + "    g2= " + str(x1) + "rad")

print("The distance between these points is: " + str(r) + "km")