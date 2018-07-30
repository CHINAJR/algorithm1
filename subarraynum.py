import random
def GenerateRandomList(number, size):
	temp = []
	random_legth = random.randint(5, size)
	current_length = 0
	while current_length < random_legth:
		temp.append(random.randint(1, number))
		current_length += 1
	return temp

def Num(arr,num):
	if arr == None or len(arr) == 0:
		return 0
	mins = [0]
	maxs = [0]
	result = 0
	r = 0
	for i in range(len(arr)):
		while r < len(arr):#更新最小队列，记录坐标
			while len(mins) != 0 and arr[mins[-1]] >= arr[r]:
				mins.pop()                                                                       
			mins.append(r)
			while len(maxs) != 0 and arr[maxs[-1]] <= arr[r]:
				maxs.pop()
			maxs.append(r)
			if arr[maxs[0]] - arr[mins[0]] > num:
				break
			r += 1
		if mins[0] == i:
			mins.pop(0)
		if maxs[0] == i:
			maxs.pop(0)
		result += r-i
	return result

def duishu(arr,num):

	if arr == None or len(arr) == 0:
		return 0
	res = 0 
	for i in range(len(arr)):
		ar = []
		for j in range(i,len(arr)):

			ar.append(arr[j])
			if max(ar)-min(ar) <= num:
				res += 1
	return res


if __name__ == '__main__':
	for i in range(20):
		l = GenerateRandomList(20, 10)
		standard_l = duishu(l,3)
		result = Num(l,3)
		print( result == standard_l)
