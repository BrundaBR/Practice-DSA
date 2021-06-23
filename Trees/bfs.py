class TreeNode:
	def __init__(self,data):
		self.val=data
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
				if data < cur.val:
					if cur.left:
						cur=cur.left
					else:
						cur.left=TreeNode(data)
						break
				elif data > cur.val:
					if cur.right:
						cur=cur.right
					else:
						cur.right=TreeNode(data)
						break
				else:
					break

def Breadthfirstsearch(root):
	q=[root]
	result=[]
	while q!=[]:
		size=len(q) # nodes to process
		currentlevel=[]
		for i in range(size):
			current=q.pop(0)
			currentlevel.append(current.val)
			if current.left:
				q.append(current.left)
			if current.right:
				q.append(current.right)
		result.append(currentlevel)
	print(result)
	
def depthfirstsearch(root):
	if root is None:
		return 
	stack=[root]
	result=[] # 2 5 7 21 9 1
	while stack!=[]:
		current=stack.pop()
		result.append(current.val)
		if current.left:
			stack.append(current.left)
		if current.right:
			stack.append(current.right)
	print(result)



instance=BinaryTree()
instance.insert(2)
instance.insert(1)
instance.insert(5)
instance.insert(7)
instance.insert(21)
instance.insert(9)
Breadthfirstsearch(instance.root)
depthfirstsearch(instance.root)