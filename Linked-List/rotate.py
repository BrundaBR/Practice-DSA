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



	def rotate(self,p):
		first=self.head
		cur=self.head
		idx=1
		end=self.head
		while end.next: 
			end=end.next
		while cur and idx!=p:
			idx+=1
			cur=cur.next
		end.next=first
		self.head=cur.next
		cur.next=None




instance=Linkedlist()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.rotate(2)