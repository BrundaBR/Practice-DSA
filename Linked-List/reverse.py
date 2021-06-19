

class Node:
	def __init__(self,data):
		self.val=data
		self.next=None

class LinkedList:

	def __init__(self):
		self.head=None

	def insert(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			cur=self.head
			while cur.next:
				cur=cur.next
			cur.next=Node(data)



	def display(self,head):
		cur=head
		while cur:
			print(cur.val,end="->")
			cur=cur.next

	def reverse(self,head):
		stack=[]
		c=head
		while c:
			stack.append(c.val)
			c=c.next

		dummy=Node(0)
		cur=dummy
		while stack!=[]:
			ele=stack.pop()
			cur.next=Node(ele)
			cur=cur.next
		self.display(dummy.next)

instance=LinkedList()
instance.insert(1)
instance.insert(2)
# instance.display(instance.head)
instance.reverse(instance.head)