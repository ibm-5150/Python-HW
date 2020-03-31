a = 500
sum_x = 0
n = 1

day_30 = round(a*((1 + 10/100)**30))
print(f"Day 30: {day_30}m")

while True:

	n = n + 1
	an = round(500*((1 + 10/100)**n))
	if n >= 30:
		break
	
for x in range(an):
	a = a * 1.1 
	sum_x = round(sum_x + a)
	if sum_x >= 42000:
		break

print(f"Days to exceed marathon: {x} ({sum_x}m)")



