'''
Question : Find a element in linkedlist and return 
"yes" if found and "NO" if no found
Example:
	find=4
	1->2->3->4->Null
	find=10
	1->2->3->4->Null

Question: Find element before and after the value to 
be deleted

Example: 
	del=4
	1->2->3->4->Null

	return 3 and null

	del=10
	1->2->3->4->Null
	return "Not found"
	

'''

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


	def search(self,f):
		cur=self.head
		while cur:
			if cur.val==f:
				return "YES"
			else:
				cur=cur.next
		return "NO"

	def display(self):
		cur=self.head
		while cur:
			print(cur.val,end="->")
			cur=cur.next

	def delete(self,d):
		cur=self.head
		fast=cur.next
		slow=cur
		prev=0
		after=[]
		while fast!=None:
			if fast.val==d:
				prev+=slow.val
				if fast.next==None:
					after.append("None")
					slow.next=None
				else:
					after.append(fast.next.val)
					slow.next=fast.next
					fast.next=None
			fast=fast.next
			slow=slow.next
		after=after[0]
		return prev,after

	def nback(self,n):
		cur=self.head
		dummy=Node(0)
		dummy.next=cur
		slow=dummy
		fast=dummy

		for _ in range(n+1):
			fast=fast.next
		while fast!=None:
			fast=fast.next
			slow=slow.next
		slow.next=slow.next.next

instance=LinkedList()
instance.insert(1)
instance.insert(2)
instance.insert(3)
instance.insert(4)
instance.insert(5)

# print(instance.search(2))
instance.display()
# print(instance.delete(2))
# instance.nback(2)
instance.display()

