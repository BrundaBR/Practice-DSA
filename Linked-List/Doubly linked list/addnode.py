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
			while cur.next:
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



	def add_before(self,val):
		cur=self.head
		new_node=ListNode(val)
		while cur:
			if cur.prev is None and cur.val==val:
				self.prepend(val)
			elif  cur.val==val:
				prev=cur.prev
				cur.prev=new_node
				new_node.next=cur
				new_node.prev=prev
			cur=cur.next
			


	def add_after(self,val):
		#prepend is after
		
		cur=self.head
		while cur:
				# for 1 element
			if cur.next is None and  cur.val==val:
				self.append(val)
			elif cur.val==key:
				new_node=ListNode(val)
				nxt=cur.next #save
				cur.next=new_node
				new_node.prev=cur
				new_node.next=nxt
				nxt.prev=new_node
				return 
			cur=cur.next

			




instance=DoublyLinkedList()

instance.append(1)
instance.append(2)
instance.append(3)
instance.append(4)
instance.append(5)

# instance.display()