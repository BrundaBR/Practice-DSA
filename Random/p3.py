'''
1. divide the list into sets of 3
2. check for conditions
3. retun unique list

'''
def threesum(l):
	# base case
	if len(l)==0 or len(l)==1: 
		return []
	#divide list of 3
	strip=3
	the_list=[]
	for i in range(len(l)):
		x=l[i]
		xs = l[:i] + l[i+1:]
		for p in threesum(xs):
			the_list.append([x] + p)
	print(the_list)


	# the  strip 
	# for i in range(len(l)):
	# 	y=i+3
	# 	if y < len(l):
	# 		d=l[i:y]
	# 		the_list.append(d)
	x=0
	y=1
	z=2
	# the check
	for i in the_list:
		if i[x]!=i[y] and i[y]!=i[z] and i[x]!=i[z]:
			if i[x]+i[y]+i[z]==0:
				print(i)





lis=[-1,0,1,2,-1,-4]
print(threesum(lis))