def printmatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j],end=' ')
		print()

def printMatrixZigZag(matrix):
	x1 = 0 
	x2 = 0 
	x3 = len(matrix)-1
	x4 = len(matrix[0])-1
	direct = True
	a=0
	while x1 <= x3 and x2 <= x4:
		x = printLevel(matrix,x1,x2,x3,x4,direct)
		x1 = x[0]
		x2 = x[1]
		direct = not direct
		if direct :
			x1 += 1
			if x1 > x3:
				x1 -= 1
				x2 += 1
		else:
			x2 += 1
			if x2 > x4:
				x2 -= 1
				x1 += 1

def printLevel(matrix,x1,x2,x3,x4,direct):
	if direct:
		while x1 <= x3 and x2 >= 0:
			print(matrix[x1][x2],end=' ')
			if x1 - 1 >= 0 and x2 + 1 <= x4:
				x1 -= 1 
				x2 += 1
			else:
				return (x1,x2)
	else:
		while x1 >= 0 and x2 <= x4:
			print(matrix[x1][x2],end=' ')
			if x1 + 1 <= x3 and x2 - 1 >= 0:
				x1 += 1 
				x2 -= 1
			else:
				return (x1,x2)


if __name__ == '__main__':
	matrix = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ] ];
	printmatrix(matrix)
	print()
	matrix1 = printMatrixZigZag(matrix)
	print()
