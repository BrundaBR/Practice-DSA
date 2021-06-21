

def increment(a):
	last=a[-1]+1
	if last > 9:
		x_list=list(map(int,str(last)))
		x,y=x_list[0],x_list[1]
		a[-2]+=x
		a[-1]=y
		return a
	

		


print(increment([1,3,9]))