def getNext(str2):
	'''计算str2的最后一位返回后缀'''
	nexts = [0 for i in range(len(str2)+1)]
	nexts[0] = -1
	k = -1
	i = 0
	while i < len(str2):
		if str2[k] == str2[i] or k == -1:
			k += 1
			i += 1
			nexts[i] = k
		else:
			k = nexts[k] 
	return nexts[len(nexts)-1]

def answer(str2):
	if str2 == None or len(str2) == 0:
		return ''
	if len(str2) == 1:
		return str2+str2
	if len(str2) == 2:
		if str2[0] == str2[1]:
			return str2 +str2[0]
		else:
			return str2+str2
	nexts = getNext(str2)
	return str2 + str2[nexts:]
if __name__ == '__main__':
	print(answer('abcbab'))
