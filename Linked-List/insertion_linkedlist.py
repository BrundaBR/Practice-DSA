class Node:
	def __init__(self,data):
		self.next=None
		self.data=data


class LinkedList:
	def __init__(self):
		self.head=None

	def append(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			cur=self.head
			while cur.next:
				cur=cur.next
			cur.next=Node(data)


	def prepend(self,data):
		if self.head is None:
			self.head=Node(data)
		else:
			new_node=Node(data)
			new_node.next=self.head
			self.head=new_node

	def printfun(self):
		cur=self.head
		while cur:
			print(cur.data,end=" ")
			cur=cur.next

instance=LinkedList()
instance.append(2)
instance.append(4)
instance.append(6)
instance.printfun()
instance.prepend(1)
instance.printfun()
