import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def sorts(alist,l,r):
	for i in range(l,r):
		for j in  range(i+1,r+1):
			if alist[i] > alist[j]:
				alist[i],alist[j] = alist[j],alist[i]

def findMedian(alist,l,r):
	i = l
	index = 0
	while i + 4 <= r:#5个一组
		sorts(alist,i,i+4)
		alist[l+index],alist[i+2] = alist[i+2],alist[l+index]
		i += 5
		index += 1
	if i <= r:
		sorts(alist,i,r)
		alist[l+index],alist[i+(r-i)//2] = alist[i+(r-i)//2],alist[l+index]
		index += 1
	if index == 1:
		return alist[l]
	else:
		return findMedian(alist,l,l+index) 



def findKthMin(alist,l,r,k):
	medieVal = findMedian(alist,l,r)
	medieVal = alist[l]
	i = l
	j = r
	#快排
	while(i<j):		
		while i < j and alist[j] > medieVal:			
			j -= 1
		alist[i] = alist[j]
		while i < j and alist[i] <= medieVal:
			i += 1
		alist[j] = alist[i]
	alist[i] = medieVal

	if i-l+1 == k:
		return alist[i]
	elif i-l+1 > k:
		return findKthMin(alist,l,i-1,k)
	else:
		return findKthMin(alist,i+1,r,k-(i-l+1))

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = sorted(l)
		ans = standard_l[3]
		result = findKthMin(l,0,len(l)-1,4)
		print( result == ans)
