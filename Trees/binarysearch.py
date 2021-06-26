class TreeNode:
	def __init__(self,val):
		self.val=val
		self.right=None
		self.left=None

class BinarySearchTree:
	def __init__(self):
		self.root=None

	def insert_in_bst(self,val):
		if self.root is None:
			self.root=TreeNode(val)

		cur=self.root
		while True:
			if val < cur.val:
				if cur.left:
					cur=cur.left
				else:
					cur.left=TreeNode(val)
					break
			elif val > cur.val:
				if cur.right:
					cur=cur.right
				else:
					cur.right=TreeNode(val)
					break
			else:
				break


	def Binary_search_element(self,root,target):
		if root is None:
			return []
		while root.val != target:
			if root.left:
				root=root.left
			if root.right:
				root=root.right
		result=[]
		result.append(root.val)
		if root.left:
			result.append(root.left.val)
		if root.right:
			result.append(root.right.val)
		print(result)



instance=BinarySearchTree()
instance.insert_in_bst(4)
instance.insert_in_bst(2)
instance.insert_in_bst(7)
instance.insert_in_bst(1)
instance.insert_in_bst(3)
instance.Binary_search_element(instance.root,3)