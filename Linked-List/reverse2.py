
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

		
#inserting node a beginning of list
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

	def reverse(self,k):
		def reverse_dum(head):
			curr=head
			prev=None
			nex=None
			while curr:
				#save
				nex=curr.next
				#reverse
				curr.next=prev
				#advance
				prev=curr
				curr=nex
			return prev
		
		cur=self.head
		final_dummy=Node(0)
		reverse_dummy=Node(0)
		g1=self.head
		prev=None
		g=0

		






instance=Linkedlist()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.display()
instance.reverse(2)
instance.display()
