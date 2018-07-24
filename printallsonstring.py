def process(string,i,cha):
	'''打印字符串全子列'''
	if i == len(string):
		print(cha)
		return
	tmp = cha
	cha += ' '
	process(string,i+1,cha)
	tmp += string[i]
	process(string,i+1,tmp)
process('abc',0,'')
