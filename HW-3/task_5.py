price = 10
print("Price for 1kg of oranges is: {} $".format(price))

buy = (input("Insert amount of kg to check price: "))


while int(buy) > 0:
    print('"while" result: ' + str(price * int(buy))) 
    break


for x in buy:
	print('"for" result: ' + str(price * int(buy)))
	break