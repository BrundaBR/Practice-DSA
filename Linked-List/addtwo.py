class Node:
	def __init__(self,data):
		self.val=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def insert(self,data):
		if self.head==None:
			self.head=Node(data)
		else:
			cur=self.head
			while cur.next:
				cur=cur.next
			cur.next=Node(data)

	def display(self,head):
		while head:
			print(head.val,end="->")
			head=head.next

def addtwo(left,right):
    stack1=[]
    stack2=[]
    while l1:
        stack1.append(str(l1.val))
        l1=l1.next
    while l2:
        stack2.append(str(l2.val))
        l2=l2.next
    
    x=int(''.join(stack1[::-1]))
    y=int(''.join(stack2[::-1]))
    res=reversed(str(x+y))
    dummy=ListNode(0)
    head=dummy
    for  i in res:
        head.next=ListNode(i)
        head=head.next
    return dummy.next
	

instance=LinkedList()
instance.insert(2)
instance.insert(4)
instance.insert(3)

instance1=LinkedList()
instance1.insert(5)
instance1.insert(6)
instance1.insert(4)
# instance.display(instance.head)
addtwo(instance.head,instance1.head)