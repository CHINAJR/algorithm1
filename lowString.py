def lowestString(strs,start,end):
	if strs == None or len(strs) == 0:
		return ''
	res = ''
	sorts(strs,start,end)
	print(strs)
	for i in range(len(strs)):
		res += strs[i]
	print(res)

def sorts(strs,start,end):
	if start >= end:
		return
	l = start
	r = end 
	mid = strs[start]
	while l < r:
		while l<r and strs[r] >= mid:
			r -= 1
		strs[l] = strs[r]
		while l<r and strs[l] <= mid:
			l += 1
		strs[r] = strs[l]
	strs[r] = mid
	sorts(strs,start,r-1)
	sorts(strs,r+1,end)

if __name__ == '__main__':
	strs1 = [ "jibw", "ji", "jp", "bw", "jibw" ]
	lowestString(strs1,0,len(strs1)-1)

	strs2 = [ "ba", "b" ]
	lowestString(strs2,0,len(strs2)-1)
	

