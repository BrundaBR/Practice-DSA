import operator
def fun(a):
	dic={}
	for i in a:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
			# to receve max item
			#max_key = max(stats, key = stats.get)
	max_val=max(dic.items(),key=operator.itemgetter(1))[0]
	print(max_val)
		




array=[1,1,2,2,2,2]
fun(array)