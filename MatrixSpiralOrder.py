def printmatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j],end=' ')
		print()

def spiralorderPrint(matrix):
	x1 = 0 #当前横坐标
	x2 = 0 #当前纵坐标
	x3 = len(matrix)-1
	x4 = len(matrix[0])-1
	while x1 <= x3:
		printEdge(matrix,x1,x2,x3,x4)
		x1 += 1
		x3 -= 1
		x4 -= 1
		x2 += 1
		print()

def printEdge(matrix,x1,x2,x3,x4): 
	for i in range(x4-x1):
		print(matrix[x1][x2+i],end=' ')
	for i in range(x3-x2):
		print(matrix[x1+i][x4],end=' ')
	for i in range(x4-x1):
		print(matrix[x3][x4-i],end=' ')
	for i in range(x3-x2):
		print(matrix[x3-i][x2],end=' ')

if __name__ == '__main__':
	matrix = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ],
				[ 13, 14, 15, 16 ] ];
	printmatrix(matrix)
	print()
	matrix1 = spiralorderPrint(matrix)
	print()




