class Node:

	def __init__(self,val=-1,lasts=None,nexts=None):
		self.nexts = nexts
		self.lasts = lasts
		self.val = val

class NodeLinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self,head):
		if head == None:
			return 

		if self.head == None:
			self.head = head 
			self.tail = head
		else:
			self.tail.nexts = head
			head.lasts = self.tail
			self.tail = head

	def moveToTail(self,head):
		if self.tail == head:
			return

		if self.head == head:
			self.head = self.head.nexts
			self.head.lasts = None
		else:
			head.lasts.nexts = head.nexts
			head.nexts.lasts = head.lasts
		head.lasts = self.tail
		head.nexts = None
		self.tail.nexts = head
		self.tail = head

	def removeHead(self):
		if self.head == None:
			return None

		res = self.head
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.head = res.nexts
			res.nexts = None
			self.head.lasts = None

		return res

class Map:
	def __init__(self,cap):
		self.keymap = {}
		self.nodemap = {}
		self.cap = cap
		self.nodelist = NodeLinkedList()

	def get(self,key):
		if self.keymap.get(key) != None:
			res = self.keymap.get(key)
			self.nodelist.moveToTail(res)
			return res.val
		return None

	def set(self,key,val):
		if self.keymap.get(key) != None:
			head = self.keymap.get(key)
			head.val = val
			self.nodelist.moveToTail(head)
		else:
			head = Node(val)
			self.keymap[key] = head
			self.nodemap[head] = key
			self.nodelist.addNode(head)
		if self.cap+1 == len(self.keymap):
			self.removeMostUnuseCache()

	def removeMostUnuseCache(self):
		res = self.nodelist.removeHead()
		reskey = self.nodemap.get(res)
		del self.nodemap[res]
		del self.keymap[reskey]

if __name__ == '__main__':
	ma = Map(3)
	ma.set('a',1)
	ma.set('b',2)
	ma.set('c',3)
	print(ma.get('b'))
	ma.set('a',8)
	print(ma.get('a'))
	ma.set('d',4)
	print(ma.get('d'))
	print(ma.get('c'))
