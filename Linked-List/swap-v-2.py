 
 
 
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


	def swap(self,k):
		def length(cur):
			l=0
			while cur:
				l+=1
				cur=cur.next
			return l
		cur=self.head
		x=length(cur)
		first=k
		idx=1
		last=x-k+1
		if first == last:
			return
		prev_f=None
		curr_1=self.head
		while curr_1 and idx != first:
			prev_f=curr_1
			curr_1=curr_1.next
			idx+=1
		#found first idx values
		prev_l=None
		curr_2=self.head
		idx_2=1
		while curr_2 and idx_2!=last:
			prev_l=curr_2
			curr_2=curr_2.next
			idx_2+=1
		#found second 

		if not curr_1 and not curr_2:
			return

		# previous
		if prev_f:
			prev_f.next=curr_2
		if prev_l:
			prev_l.next=curr_1

		curr_2.next,curr_1.next=curr_1.next,curr_2.next









instance=Linkedlist()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.insert(5)
instance.display()
instance.swap(2)
instance.display()