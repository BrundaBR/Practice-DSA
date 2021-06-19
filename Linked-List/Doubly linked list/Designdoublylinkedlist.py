#NOde structure
class ListNode:
	def __init__(self,val):
		self.prev=None
		self.next=None
		self.val=val

class DoublyLinkedList:
	def __init__(self):
		self.head=None

	def append(self,val):
		new_node=ListNode(val)
		if self.head is None:
			self.head=new_node
		else:
			cur=self.head
			while cur:
				cur=cur.next
			cur.next=new_node
			new_node.prev=cur


	def prepend(self,val):
		new_node=ListNode(val)
		cur=self.head
		cur.prev=new_node
		new_node.next=cur
		self.head=new_node
		new_node.prev=None

	def display(self):
		cur=self.head
		while cur:
			print(cur.val)
			cur=cur.next
			




instance=DoublyLinkedList()
instance.append(2)
instance.prepend(1)
instance.display()