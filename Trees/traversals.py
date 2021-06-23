class TreeNode:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None


class BST:
	def __init__(self):
		self.root=None


	def insert(self,val):
		if self.root is None:
			self.root=TreeNode(val)
		else:
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
		return



def preorder(root):
	if root:
		print(root.val,end=" ")
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		
		preorder(root.left)
		preorder(root.right)
		print(root.val,end=" ")


def inorder(root):
	if root:
		preorder(root.left)
		print(root.val,end=" ")
		preorder(root.right)
		




instance=BST()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.insert(5)
instance.insert(6)
preorder(instance.root)
print("\n")
postorder(instance.root)
print("\n")
inorder(instance.root)
