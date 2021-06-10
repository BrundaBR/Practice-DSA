class TreeNode:
	def __init__(self,data):
		self.info=data
		self.left=None
		self.right=None

class BinaryTree:
	def __init__(self):
		self.root=None

	def insert(self,data):
		if self.root is None:
			self.root=TreeNode(data)
		else:
			cur=self.root
			while True:
				if data < cur.info:
					if cur.left:
						cur=cur.left
					else:
						cur.left=TreeNode(data)
						break
				elif data > cur.info:
					if cur.right:
						cur=cur.right
					else:
						cur.right=TreeNode(data)
						break
				else:
					break

def levelorder(root):
	result=[]
	q=[root]
	while q!=[]:

		val=q.pop(0)
		# result.append([val.info])

		if val.left:
			q.append(val.left)
		if val.right:
			q.append(val.right)
	print(result)


def search(root,val):
	if root.info==val:
		return True
	cur=root
	while True:
		if val < cur.info:
			if cur.left:
				search(cur.left,val)
		
		elif val> cur.info:
			if cur.right:
				search(cur.right,val)
		else:
			break
	return False

def preorder():
	pass
def inorder():
	pass
def postorder():
	pass

instance=BinaryTree()
instance.insert(2)
instance.insert(5)
instance.insert(7)
instance.insert(21)
instance.insert(9)
# levelorder(instance.root)
search(instance.root,9)

