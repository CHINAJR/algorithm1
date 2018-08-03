def maxlength(arr,aim):
	if len(arr) == 0 or arr == None:
		return 0 

	maps = {}
	maps[0] = -1
	sums = 0 
	length =0
	for i in range(len(arr)):
		sums += arr[i]
		if maps.get(sums-aim) != None:
			length = max(length,(i-maps.get(sums-aim)))
		if maps.get(sums) == None:
			maps[sums] = i
	return length

print(maxlength([7,3,2,1,1,7,7,7],7))
