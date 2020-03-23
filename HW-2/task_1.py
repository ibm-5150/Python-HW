a = int(input("Insert a: "))
b = int(input("Insert b: "))

a_positive = bool(a > 0)
print("Number a is positive: " + str(a_positive))

a_pair = bool(a % 2 == 0)
print("Number a is pair: " + str(a_pair))

a_multiple = bool(a % 13 == 0)
print("Number a is multiple of 13: " + str(a_multiple))

a_b_pair = bool(a % 2 == 0 and b % 2 == 0)
print("Numbers a, b are pair: " + str(a_b_pair))

a_b_even_odd = bool(a % 2 == 0 and b % 2 == 0 or a % 2 != 0 and b % 2 != 0)
print("Numbers a, b are even: " + str(a_b_even_odd))