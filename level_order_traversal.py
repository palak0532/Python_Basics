class Node:

 	def __init__(self,key):
 		self.left= None
 		self.right = None
 		self.value = key


def findheight(root):
	h = height(root)
	return h


def height(root):

	if root == None:
		return 0
	else:
		left_height = height(root.left)
		right_height = height(root.right)
		h = max(left_height, right_height)
		h = h+1
		return h

def levelorder(root, level):

	if root == None:
		return
	if(level ==1):
		print(root.value)
	elif(level > 1):
		levelorder(root.left, level-1)
		levelorder(root.right, level-1)
	
def printlevel(root):
	h = height(root)
	for i in xrange(1, h+1):
		levelorder(root, i)
		print "\n"


root = Node(10)
root.left = Node(6)
root.left.left = Node(5)
root.left.right = Node(7)
root.right = Node(12)
root.right.left  = Node(11)
root.right.right  = Node(13)

printlevel(root)
