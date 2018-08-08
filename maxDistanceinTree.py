class Type:
	def __init__(self,m,h):
		self.m = m 
		self.h = h 

class Node(object):
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.left = lchild
		self.right = rchild

def maxDistance(head):
	if head == None:
		ab = Type(0,0)		
		return ab
	left = maxDistance(head.left)
	right = maxDistance(head.right)
	includeHeadDistance = left.h + 1 + right.h
	p1 = left.m
	p2 = right.m
	res = max(max(p1,p2),includeHeadDistance)
	hit = max(left.h,right.h)+1
	aa = Type(res,hit)
	return  aa
