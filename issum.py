def money1(alist,aim):
	return process(alist,0,0,aim)

def process(alist,i,sums,aim):
	if sums == aim:
		return True
	if i == len(alist):
		return False
		#选择是否加入当前数
	return process(alist,i+1,sums,aim) or process(alist,i+1,sums+alist[i],aim)


alist = [2,2,8]
aim = 12
print(money1(alist,aim))
