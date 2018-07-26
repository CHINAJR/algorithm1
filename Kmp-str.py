def getNext(str2):
	'''位置数组，通过计算最长前后缀，确定回移的最小位置，加速计算'''
	k = -1 
	nexts = [0 for i in range(len(str2))]
	nexts[0] = -1
	i = 0
	while i < len(str2)-1:
		if k == -1 or str2[i] == str2[k]:
			i += 1
			k += 1
			nexts[i] = k
		else:
			k = nexts[k]
	return nexts

def getIndex(str1,str2):
	nexts = getNext(str2)
	i1 = 0 
	i2 = 0 
	while i1 < len(str1) and i2 < len(str2):
		if str1[i1] == str2[i2]:
			i1 += 1 
			i2 += 1
		elif nexts[i2] == -1:
			i1 += 1
		else:
			i2 = nexts[i2]
	if i2 == len(str2):
		return i1-i2
	else:
		return -1

if __name__ == '__main__':
	 s1 = 'ababababca'
	 s2 = 'abababca'
	 print(getIndex(s1,s2))		
