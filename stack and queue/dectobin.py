
'''
Step-1 : run loop till quotient is 0
	Store the quotient and remainder and particularly remainder in stack
Step2: create and empty string ,add each ele of stack till its empty

'''
def decimaltobinary(x):
	result=""
	stack=[] #0 
	 # [124,121,60,30,15,7,3]
	if x==0:return 0
	while x > 0:
		r=x%2
		stack.append(r)
		x=x//2
			
	while stack!=[]:
		result+=str(stack.pop())
	return result
x=124
print(decimaltobinary(x))