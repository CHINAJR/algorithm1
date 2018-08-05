def mostEOR(arr):
	'''异或最长子数组 '''
	ans = 0
	xor = 0
	most = [0 for i in range(len(arr))]
	maps = {}
	maps[0] = -1
	for i in range(len(arr)):
		xor = xor^arr[i]
		if maps.get(xor) != None:
			pre = maps.get(xor)
			if pre == -1:
				most[i] = 1
			else:
				most[i] = most[pre]+1
		if i > 0:
			most[i] = max(most[i-1],most[i])
		maps[xor] = i 
		ans = max(ans,most[i])
	return ans


print(mostEOR([1,2,3,0,3,2,1]))
