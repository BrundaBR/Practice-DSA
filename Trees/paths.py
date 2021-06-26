class TreeNode:
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

class BST:
	def __init__(self):
		self.root=None


	def insert(self,val):
		if self.root is None:
			self.root=TreeNode(val)
		else:
			cur=self.root
			while True:
				if val<cur.val:
					if cur.left:
						cur=cur.left
					else:
						cur.left=TreeNode(val)
						break
				elif val>cur.val:
					if cur.right:
						cur=cur.right
					else:
						cur.right=TreeNode(val)	
						break
				else:
					break
			return
	
	def helper(self,root,res,path):
		res=[]
		if root==None:
			return
		path.append(root.val)
		if root.left==None and root.right==None:
			res.append(path)
		self.helper(root.left,res,path)
		self.helper(root.right,res,path)
		path.pop()
		


	def allpaths(self,root):
		self.res=[]
		self.path=[]
		self.helper(root,self.res,self.path)
		return self.res









instance=BST()
instance.insert(7)
instance.insert(5)
instance.insert(4)
instance.insert(1)
instance.insert(3)
print(instance.allpaths(instance.root))