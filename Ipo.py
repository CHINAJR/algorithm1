import queue as Q 

def findCapital(cost,profit,w):
	while not cost.empty():
		item = cost.get()
		if item[0] < w:
			profit.put(item)
			profit = sorts(profit)
			w += profit.get()[0]
		else:
			cost.put(item)
			return w

def sorts(profit):
	alist = []
	for i in range(profit.qsize()):
		alist.append(profit.get())
	if profit.empty():
		for i in range(len(alist)):
			profit.put((alist[i][1],alist[i][0]))
	return profit

if __name__ == '__main__':
	cost = Q.PriorityQueue()
	profit = Q.PriorityQueue()
	cost.put((10,12))
	cost.put((100,13))
	cost.put((12,14))
