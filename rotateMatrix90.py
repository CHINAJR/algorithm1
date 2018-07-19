def rotate(matrix):
	x1 = 0
	y2 = len(matrix[0])-1 
	while y2 > x1 :
		rotateEdge(matrix,x1,y2)
		x1 += 1 
		y2 -= 1
	return matrix
		
def rotateEdge(matrix,x1,y2):
	time = y2-x1
	for i in range(time):
		tmp = matrix[x1+i][y2]
		matrix[x1+i][y2] = matrix[x1][x1+i]
		matrix[x1][x1+i] = matrix[y2-i][x1] 
		matrix[y2-i][x1] = matrix[y2][y2-i]
		matrix[y2][y2-i] = tmp

def printmatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j],end=' ')
		print()

if __name__ == '__main__':
	matrix = [ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ],
				[ 13, 14, 15, 16 ] ];
	printmatrix(matrix)
	print()
	matrix1 = rotate(matrix)
	printmatrix(matrix1)
	print()
