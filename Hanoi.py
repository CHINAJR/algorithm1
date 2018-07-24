def hanoi(n):
	if n > 0 :
		func(n,n,'left','mid','right')

def func(rest,do,start,helps,to):
	if rest == 1:
		print('move [%d] from [%s] to [%s]'%(do,start,to))
	else:
		func(rest-1,do-1,start,to,helps)
		func(1,do,start,helps,to)
		func(rest-1,do-1,helps,start,to)

if __name__ == '__main__':
	hanoi(3)
