file_in = open('task_3.txt','r')
file_out = open('task_3_out.txt','w')
first_line = file_in.readline()

for line in file_in:
	file_out.write(line.replace(first_line,''))
file_in.close()
file_out.close()