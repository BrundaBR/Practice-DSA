
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


	def swap(self,val_1,val_2):
		# Check if both values are same
		if val_1 == val_2:
			return
		# set pointer for first node
		prev_1=None
		curr_1=self.head
		while curr_1.data!=val_1:
			prev_1=curr_1
			curr_1=curr_1.next
		# we have val tht matches the node
		#Repeat for second node
		prev_2=None
		curr_2=self.head
		while curr_2.data!=val_2:
			prev_2=curr_2
			curr_2=curr_2.next
		if not curr_2 and not curr_1:
			return

		# set previous values
		if prev_1:
			# 2->3
			prev_1.next=curr_2

		if prev_2:

			prev_2.next=curr_1
		# swapp
		curr_2.next ,curr_1.next = curr_1.next , curr_2.next

		


instance=Linkedlist()
instance.insert(1)
instance.insert(2)
instance.insert(4)
instance.insert(3)
instance.insert(5)
instance.display()
instance.swap(2,3)
instance.display()