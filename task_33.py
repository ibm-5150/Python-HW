import math

b_price = 3.49

#one_percent = 3.49/100
#discount_1 = 3.49-(one_percent*60)

user_bread = int(input())
regular_price = user_bread * b_price
discount = ((user_bread * b_price) / 100) * 60 
user_price = (user_bread * b_price) - discount

r_p = round(regular_price, 2)
u_d = round(discount, 2)
u_p = round(user_price, 2)


print("Original price of " + str(user_bread) + " loaves of bread is: " + str(r_p)+"$")
print("The discount is: " + str(u_d) + "$")
print("Total price is: " + str(u_p)+"$")


