
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
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
		return

	def display(self):
		cur=self.head
		while cur:
			print(cur.data,"->",end="")
			cur=cur.next
		print("None")

	def insert_start(self,data):
		cur=self.head
		new_node=Node(data)

		new_node.next=cur
		self.head=new_node

	def delete(self,data):
		cur=self.head
		while cur.next.data!=data:
			cur=cur.next
		cur.next=cur.next.next
def display(head):
	while head:
		print(head.data)
		head=head.next
def merge(h1,h2):
	print(h1.data,h2.data)
	final_dummy=Node(0)
	head=final_dummy
	while h1 and h2:
		if h1.data < h2.data:
			final_dummy.next=h1
			h1=h1.next
			final_dummy=final_dummy.next
		else:
			final_dummy.next=h2
			h2=h2.next
			final_dummy=final_dummy.next
	if h1:
		final_dummy.next=h1
	if h2:
		final_dummy.next=h2

	return head.next
	


instance=Linkedlist()
instance.insert(1)
instance.insert(2)
instance.insert(4)
instance.insert(3)
instance.insert(5)
# instance.display()
instance2=Linkedlist()
instance2.insert(6)
instance2.insert(7)
instance2.insert(8)
instance2.insert(9)
instance2.insert(10)
# instance2.display()
merge(instance.head,instance2.head)