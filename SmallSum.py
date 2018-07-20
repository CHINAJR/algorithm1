import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def SmallSum(alist):
	if len(alist)<= 1:
		return 0
	return MergeSort(alist,0,len(alist)-1)

def MergeSort(alist,l,r):
	if l == r :
		return 0 
	mid = (l+r)//2
	
	return MergeSort(alist,l,mid)+MergeSort(alist,mid+1,r)+Merge(alist,l,mid,r)

def Merge(arr,L,mid,R):
	help_list = []
	p1 = L
	p2 = mid + 1
	res = 0
	while p1 <= mid and p2 <= R:
		if arr[p1] < arr[p2]:
			res += arr[p1] * (R - p2 + 1)
			help_list.append(arr[p1])
			p1 += 1
		else:
			help_list.append(arr[p2])
			p2 += 1
	help_list += arr[p1:mid+1]
	help_list += arr[p2:R+1]
	arr[L:R+1] = help_list
	return res
	
def standard_SmallSum(arr):
	ans = 0
	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[j] < arr[i]:
				ans += arr[j]
	return ans

if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = standard_SmallSum(l)
		a = SmallSum(l)
		print(a == standard_l)
