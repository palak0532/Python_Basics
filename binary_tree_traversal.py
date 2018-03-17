class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

#left, root, right
def inordertraversal(root):

	if(root):
		inordertraversal(root.left)
		print (root.val)
		inordertraversal(root.right)

#root, left right
def __preorder__(root):
	if(root):
		print(root.val)
		__preorder__(root.left)
		__preorder__(root.right)

def __postorder__(root):
	if(root):
		__postorder__(root.left)
		__postorder__(root.righ)
		print(root.val)



root = Node(10)
root.left = Node(6)
root.left.left = Node(5)
root.left.righ = Node(7)
root.right = Node(12)
root.right.left  = Node(11)
root.right.right  = Node(13)

#inordertraversal(root)

__preorder__(root)
