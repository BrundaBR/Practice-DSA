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
		else:
			cur=self.head
			while cur.next:
				cur=cur.next
			cur.next=Node(data)
		return
	def deletion_by_val(self,val):
		#if it is head
		if self.head.data==val:
			cur=self.head
			self.head=cur.next
			cur=None

		# if not head
		else:
			cur=self.head
			while cur and cur.data!=val:
				prev=cur
				cur=cur.next
			prev.next=cur.next
			cur=None


	def display(self):
		cur=self.head
		while cur:
			print(cur.data,"->",end="")
			cur=cur.next
		print("None")


	def deletion_by_pos(self,pos):
		#if pos is 0
		if pos==0:
			cur=self.head
			self.head=cur.next
			cur=None
		else:# if pos is other than 0
			idx=0
			cur=self.head
			while cur and idx!=pos:
				prev=cur
				idx+=1
				cur=cur.next
			# we have right pos 
			prev.next=cur.next
			cur=None


instance=LinkedList()
instance.insert(1)#prev
instance.insert(10)
instance.insert(11)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.insert(5)
instance.deletion_by_val(10)
instance.deletion_by_pos(1)
instance.display()

