



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

	def oddeven(self,head):
		dummy_even=Node(0)
		e=dummy_even
		dummy_odd=Node(0)
		o=dummy_odd
		i=1
		while head:
			if i%2==0:
				#even add to even list
				e.next=head
				head=head.next
				e=e.next
				i+=1
			else:
				o.next=head
				head=head.next
				o=o.next
				i+=1
			
		#link both list
		e.next=None
		o.next=dummy_even.next
		self.display(dummy_odd.next)

	def display(self,head):
		cur=head
		while cur:
			print(cur.val,end="->")
			cur=cur.next

instance=LinkedList()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.insert(5)
# instance.display()
print("\n")
instance.oddeven(instance.head)
