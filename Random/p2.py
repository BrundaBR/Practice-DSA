
'''

nums is given
if val>1 return true
otherwise false


'''
def fun(n):
	dic={}
	for i in n:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1

	for key,val in dic.items():
		if val>1:
			return True
			break
	return False





nums=[1,2,3,1]
print(fun(nums))