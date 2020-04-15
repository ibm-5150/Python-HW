#------------
#NOT FINISHED
#------------
matrix = list()
for _ in range(8):
	matrix_list = list()
	for _ in range(8):
		matrix_list.append(0)
	matrix.append(matrix_list)
print(matrix)

"""
92 total solutions; https://en.wikipedia.org/wiki/Eight_queens_puzzle

5 x 5 

x 0 x 0 x
0 x x x 0
x x 1 x x
0 x x x 0
x 0 x 0 x

8 x 8 
- = 0

- - - x - - - x
x - - x - - x -
- x - x - x - -
- - x x x - - -
x x x 1 x x x x
- - x x x - - -
- x - x - x - -
x - - x - - x -
"""
