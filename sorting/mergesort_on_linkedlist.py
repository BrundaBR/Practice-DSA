'''
Apply merge sort for linked list
'''
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

	def sortList(self, head):
		if not head:
			return None
		if not head.next:
			return head
		def split(head):
			fast = head
			slow = Node(None)
			cur = slow
			while fast and fast.next:
				fast = fast.next.next
				cur.next = head
				head = head.next
				cur = cur.next
			l = cur.next
			cur.next = None
			return slow.next, l

		def merge(list1, list2):
			if not list1:
				return list2
			if not list2:
				return list1
			dummy = Node(None)
			dummyCur = dummy
			while list1 and list2:
				if list1.data < list2.data:
					dummyCur.next = list1
					list1 = list1.next
				else:
					dummyCur.next = list2
					list2 = list2.next
				dummyCur = dummyCur.next
			if list1:
				dummyCur.next = list1
			else:
				dummyCur.next = list2
			return dummy.next

		l1, l2 = split(head)
		left = self.sortList(l1)
		right = self.sortList(l2)
		return merge(left, right)

		
ins=Linkedlist()
ins.insert(4)
ins.insert(2)
ins.insert(1)
ins.insert(3)
print(ins.sortList(ins.head))

# class Solution:
# 	def sortList(self, head: ListNode) -> ListNode:
# 		if not head:
# 			return None
# 		if not head.next:
# 			return head
# 		def split(head):
# 			fast = head
# 			slow = ListNode(None)
# 			cur = slow
# 			while fast and fast.next:
# 				fast = fast.next.next
# 				cur.next = head
# 				head = head.next
# 				cur = cur.next
# 			l = cur.next
# 			cur.next = None
# 			return slow.next, l
# 		def merge(list1, list2):
# 			if not list1:
# 				return list2
# 			if not list2:
# 				return list1
# 			dummy = ListNode(None)
# 			dummyCur = dummy
# 			while list1 and list2:
# 				if list1.val < list2.val:
# 					dummyCur.next = list1
# 					list1 = list1.next
# 				else:
# 					dummyCur.next = list2
# 					list2 = list2.next
# 				dummyCur = dummyCur.next
# 			if list1:
# 				dummyCur.next = list1
# 			else:
# 				dummyCur.next = list2
# 			return dummy.next
# 		l1, l2 = split(head)
# 		left = self.sortList(l1)
# 		right = self.sortList(l2)
# 		return merge(left, right)
