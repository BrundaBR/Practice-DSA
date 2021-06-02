def fun(n):
	dic={}
	for i in range(len(n)):
		if n[i] in dic:
			dic[n[i]]+=1
		else:
			dic[n[i]]=1

	for val,key in dic.items():
		if key>1:
			print(val)




nums=[1,3,4,2,2]
fun(nums)