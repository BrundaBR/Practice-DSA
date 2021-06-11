	
class validparenthesis:
	def __init__(self):
		self.items=[]

	def checkmatches(self,op,cl):
		if op=="(" and cl==")" or op=="{" and cl=="}" or op=="[" and cl=="]":
			return True
		else:
			return False

	def open_paren(self,c):
		if c=="(" or c=="{" or c=="[":
			return True
		else:
			return False
	def validation(self,s):
		for cur in s:
			if self.open_paren(cur):
				# Adding to stack
				self.items.append(cur)
			else:
				# if it is closing
				if not self.items==[]:
					top=self.items.pop()
					if not self.checkmatches(top,cur):
						return "INVALID"
					else:
						continue
				else:return "INVALID"

		if self.items==[]:
			return "VALID"
		else:
			return "INVALID"

instance=validparenthesis()
print(instance.validation("[())"))