'''
 first non repeating index
 if no then -1

'''


def fun(s):
	dic={}
	for i in s:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	res=[]
	for val,key in dic.items():
		if key==1:
			res.append(val)

	if len(res)==0:
		return -1
	else:
		for i in range(len(s)):
			
			if s[i]==res[0]:
				return i



s="aabb"
print(fun(s))