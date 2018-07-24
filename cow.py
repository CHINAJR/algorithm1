def cowNumber(n):
	'''三年后成年能生产'''
	if n < 1:
		return 0 
	if n == 1 or n == 2 or n == 3:
		return n
	else:
		return cowNumber(n-1) +cowNumber(n-3)
