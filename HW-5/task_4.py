k = int(input("Enter amount of characters to delete in each file line: "))
file_in = open('task_4.txt','r')
file_out = open('task_4_out.txt','w')
lines = file_in.readlines()

line_symbols = list()
for x in lines:
	line_symbols.append(x[k:])

file_string = ''
for element in line_symbols:
	file_string = file_string + element

file_out.write(file_string)

file_in.close()
file_out.close()

