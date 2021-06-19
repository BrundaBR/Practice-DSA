
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	def insert(self,data):
		if self.head is None:
			self.head=Node(data)
		cur=self.head
		while cur.next:
			cur=cur.next
		cur.next=Node(data)
	def divide(self):
		head=self.head
		temp=head
		slow=head
		fast=head
		while fast!=None and fast.next!=None:
			temp=slow
			slow=slow.next
			fast=fast.next.next
		print(temp.data)
		print(slow.data)
		print(fast.data)




instance=LinkedList()
instance.insert(12)
instance.insert(24)
instance.insert(3)
instance.insert(49)
instance.divide()
