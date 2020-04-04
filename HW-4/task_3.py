import random

matrix = list()
for _ in range(3):
	matrix_list = list()
	for _ in range(4):
		matrix_list.append(random.randint(0,10))
	matrix.append(matrix_list)
#sum
matrix_sum = 0
for x in matrix:
	print(x)
	for y in x:
		matrix_sum = matrix_sum + y
print(f"Matrix sum: {matrix_sum}")
#max number
max_number = -1
for x in matrix:
	for y in x:
		if y > max_number:
			max_number = y
print(f"Matrix max number: {max_number}")
#first line sum
first_line_sum = 0
for x in matrix[0]:
	first_line_sum = first_line_sum + x
print(f"Sum of the first line: {first_line_sum}")
#second column sum
second_column_sum = matrix[0][1] + matrix[1][1] + matrix[2][1]
print(f"Second column sum: {second_column_sum}")
#minimum number
second_column = list()
for _ in range(1):
	second = list()
	for _ in range(1):
		second.append(matrix[0][1])
		second.append(matrix[1][1])
		second.append(matrix[2][1])
second_column.append(second)
min_number = 10
for x in second_column:
	for y in x:
		if y < min_number:
			min_number = y
print(f"Second column minimum numbmer: {min_number}")
#diagonal max number
diagonal = list()
for _ in range(1):
	diag = list()
	for _ in range(1):
		diag.append(matrix[0][0])
		diag.append(matrix[1][1])
		diag.append(matrix[2][2])
diagonal.append(diag)
diagonal_max = -1
for x in diagonal:
	for y in x:
		if y > diagonal_max:
			diagonal_max = y
print(f"Diagonal maximum number is: {diagonal_max}")