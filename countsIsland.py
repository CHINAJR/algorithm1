def countIslands(matrix):
	if matrix == None or matrix[0] == None:
		return 0 
	N = len(matrix)
	M = len(matrix[0])
	res = 0 
	for i in range(N):
		for j in range(M):
			if matrix[i][j] == 1 :
				res += 1
				infect(matrix,i,j,N,M) 
	return res

def infect(matrix,i,j,N,M):
	'''遍历四周，扩大岛范围'''
	if i < 0 or i >= N or j < 0 or j >= M or matrix[i][j] != 1:
		return 
	matrix[i][j] = 2
	infect(matrix,i-1,j,N,M)
	infect(matrix,i+1,j,N,M)
	infect(matrix,i,j-1,N,M)
	infect(matrix,i,j+1,N,M)

if __name__ == '__main__':
	m1 = [  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
	[ 0, 1, 1, 1, 0, 1, 1, 1, 0 ],
	[ 0, 1, 1, 1, 0, 0, 0, 1, 0 ],
	[ 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
	[ 0, 0, 0, 0, 0, 1, 1, 0, 0 ],
	[ 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
	[ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]
	m2 = [  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
	[ 0, 1, 1, 1, 1, 1, 1, 1, 0 ],
	[ 0, 1, 1, 1, 0, 0, 0, 1, 0 ],
	[ 0, 1, 1, 0, 0, 0, 1, 1, 0 ],
	[ 0, 0, 0, 0, 0, 1, 1, 0, 0 ],
	[ 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
	[ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],]
	print(countIslands(m1))
	print(countIslands(m2))
