class Node:
	def __init__(self,val):
		self.next = None
		self.val = val

def getLoopNode(head):
	if head == None or head.next == None:
		return None
	if head.next.next == None:
		return None
	n1 = head.next 
	n2 = head.next.next
	while n1 != n2:
		if n2.next == None or n2.next.next == None:
			return None
		n2 = n2.next.next
		n1 = n1.next
	n2 = head
	while n2 != n1:
		n1 = n1.next
		n2 = n2.next
	return n1

def noLoop(head1,head2):
	if head1 == None or head2 == None:
		return None
	cur1 = head1
	cur2 = head2
	n = 0
	while cur1.next != None:
		cur1 = cur1.next
		n += 1
	while cur2.next != None:
		n -= 1
		cur2 = cur2.next
	if cur1 != cur2:
		return None
	if n:
		cur1,cur2 = head1,head2
	else:
		cur1,cur2 = head2,head1
	n = abs(n)
	while n > 0:
		cur1 = cur1.next
		n = n-1
	while cur1 != cur2:
		cur1 = cur1.next
		cur2 = cur2.next
	return cur1

def bothLoop(head1,loop1,head2,loop2):
	if loop1 == loop2:
		cur1 = head1
		cur2 = head2
		n = 0 
		while cur1 != loop1:
			cur1 = cur1.next
			n = n + 1
		while cur2 != loop2:
			cur2 = cur2.next
			n = n -1
		if n>0:
			cur1,cur2 = head1,head2
		else:
			cur1,cur2 = head2,head1
		n = abs(n)
		while n > 0:
			cur1 = cur1.next
			n = n-1
		while cur1 != cur2:
			cur1 = cur1.next
			cur2 = cur2.next
		return cur1
	else:
		cur1 = loop1.next
		while cur1 != loop1:
			if cur1 == loop2:
				return loop1
			cur1 = cur1.next
		return None

def getIntersectNode(head1,head2):
	if head2 == None or head1 == None:
		return None
	loop1 = getLoopNode(head1)
	loop2 = getLoopNode(head2)
	if loop2 == None and loop1 == None:
		return noLoop(head1,head2)
	if loop1 != None and loop2 != None:
		return bothLoop(head1,loop1,head2,loop2)


if __name__ == '__main__':
	# 1->2->3->4->5->6->7->null
		head1 = Node(1)
		head1.next = Node(2)
		head1.next.next = Node(3)
		head1.next.next.next = Node(4)
		head1.next.next.next.next = Node(5)
		head1.next.next.next.next.next = Node(6)
		head1.next.next.next.next.next.next = Node(7)

		# 0->9->8->6->7->null
		head2 = Node(0)
		head2.next = Node(9)
		head2.next.next = Node(8)
		head2.next.next.next = head1.next.next.next.next.next # 8->6
		ans = getIntersectNode(head1, head2)
		print(ans.val)

		# 1->2->3->4->5->6->7->4...
		head1 = Node(1)
		head1.next = Node(2)
		head1.next.next = Node(3)
		head1.next.next.next = Node(4)
		head1.next.next.next.next = Node(5)
		head1.next.next.next.next.next = Node(6)
		head1.next.next.next.next.next.next = Node(7)
		head1.next.next.next.next.next.next = head1.next.next.next # 7->4

		# 0->9->8->2...
		head2 = Node(0)
		head2.next = Node(9)
		head2.next.next = Node(8)
		head2.next.next.next = head1.next # 8->2
		ans = getIntersectNode(head1, head2)
		print(ans.val)

		# 0->9->8->6->4->5->6..
		head2 = Node(0)
		head2.next = Node(9)
		head2.next.next = Node(8)
		head2.next.next.next = head1.next.next.next.next.next # 8->6
		ans = getIntersectNode(head1, head2)
		print(ans.val)
