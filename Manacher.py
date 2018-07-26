def ManacherString(string):
	res = [0 for i in range(len(string)*2+1)]
	a = 0
	for i in range(len(string)):
		res[a] = '#'
		res[a+1] = string[i]
		a += 2
	res[-1] = '#'
	return res

def maxLcpsLength(strings):
	if len(strings) == 0 or strings == None:
		return 0
	string = ManacherString(strings)
	arr = [0 for i in range(len(string))]
	index = -1
	pr = -1 
	maxs = 0
	for i in range(len(arr)):
		if pr > i :
			arr[i] = min(arr[2*index-i],pr-i)
		else:
			arr[i] = 1
		while i + arr[i] < len(string) and i - arr[i] >-1:
			if string[i+arr[i]] == string[i-arr[i]]:
				arr[i] += 1
			else:
				break
		if i + arr[i] > pr:
			pr = i + arr[i]
			index = i
		maxs = max(maxs,arr[i])
	return maxs-1

if __name__ == '__main__':
	str1 = "abc1234321a"
	print(maxLcpsLength(str1))
