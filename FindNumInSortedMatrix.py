def isContain(matrix,n):
	row = 0 
	col = len(matrix[0]) - 1
	while row < len(matrix) and col > -1:
		if matrix[row][col] < n:
			row += 1
		elif matrix[row][col] == n:
			return True
		else:
			col -= 1
	return False

if __name__ == '__main__':
	matrix = [	[ 0, 1, 2, 3, 4, 5, 6 ],# 0
				[ 10, 12, 13, 15, 16, 17, 18 ],# 1
				[ 23, 24, 25, 26, 27, 28, 29 ],# 2
				[ 44, 45, 46, 47, 48, 49, 50 ],# 3
				[ 65, 66, 67, 68, 69, 70, 71 ],# 4
				[ 96, 97, 98, 99, 100, 111, 122 ],# 5
				[ 166, 176, 186, 187, 190, 195, 200 ],# 6
				[ 233, 243, 321, 341, 356, 370, 380 ], ]# 7
	k = 233
	ans = isContain(matrix,k)
	print(ans)
