run = 500
run_sum = 0
marathon = 0

for x in range(1,31):
	run = round(run * 1.1)
	run_sum = run + run_sum

	if run_sum > 42000:
		marathon = round(42000 / (run_sum / 30))

print("Day 30: " + str(run) + "m")
print(f"After {marathon} days you've exceeded marathon distance(42km)")




