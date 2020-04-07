line_amount = int(input())
line_symbol = int(input())

k = line_symbol * '*'
result = line_amount * ('\n' + k)

file = open("file.txt","w")
file.write(result)
file.close()
