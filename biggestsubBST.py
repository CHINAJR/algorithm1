class Node:

	def __init__(self,val=-1,left=None,right=None):
		self.val = val 
		self.left = left
		self.right = right

class ReturnType:

	def __init__(self,size,head,mins,maxs):
		self.size = size
		self.head = head
		self.mins = mins
		self.maxs = maxs

def process(head):
	if head == None:
		return ReturnType(0,None,10000,-10000)

	left = head.left
	leftSubTreeInfo = process(left)
	right = head.right
	rightSubTreeInfo = process(right)

	includeSelf = 0 
	if leftSubTreeInfo.head == left and rightSubTreeInfo.head == right and head.val > leftSubTreeInfo.maxs and head.val < rightSubTreeInfo.mins:
		includeSelf = leftSubTreeInfo.size + 1 + rightSubTreeInfo.size

	p1 = leftSubTreeInfo.size
	p2 = rightSubTreeInfo.size
	maxsize = max(max(p1,p2),includeSelf)
	if p1 > p2:
		maxhead = leftSubTreeInfo.head
	else:
		maxhead = rightSubTreeInfo.head
	if maxsize == includeSelf:
		maxhead = head
	return ReturnType(maxsize,maxhead,min(min(leftSubTreeInfo.mins,rightSubTreeInfo.mins),head.val),max(max(leftSubTreeInfo.maxs,rightSubTreeInfo.maxs),head.val))

def printTree(root):
    print("Binary Tree:")
    printInOrder(root, 0, 'H', 17)
    
def printInOrder(root, height, s, length):
    if root is None:
        return
    printInOrder(root.right, height + 1, 'v', length)
    val = s + str(root.val) + s
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM -lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height * length) +val)
    printInOrder(root.left, height + 1, '^', length)

def getSpace(num):
    return ' ' * num

if __name__ == '__main__':
	head = Node(6)
	head.left = Node(1)
	head.left.left = Node(0)
	head.left.right = Node(3)
	head.right = Node(12)
	head.right.left = Node(10)
	head.right.left.left = Node(4)
	head.right.left.left.left = Node(2)
	head.right.left.left.right = Node(5)
	head.right.left.right = Node(14)
	head.right.left.right.left = Node(11)
	head.right.left.right.right = Node(15)
	head.right.right = Node(13)
	head.right.right.left = Node(20)
	head.right.right.right = Node(16)
	print(process(head).head.val)
	print(printTree(head))
	print(printTree(process(head).head))

