string = str(input())

if string.count('a') < 1:
	print("False")

elif string.count('a') == 1:
	print(string.find('a'))

elif string.count('a') >= 2:
	print(string.find('a'), string.rfind('a'))
    