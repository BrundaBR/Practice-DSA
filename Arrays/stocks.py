def mainstuff(lis,mini):
	ma=max(lis)
	x=ma-mini
	return x

def fun(lis):
	mini=min(lis)
	res=0
	for i in range(len(lis)):
		if lis[i]==mini:
			if i<len(lis)-1:
				li=lis[i+1:]
				x=mainstuff(li,mini)
				if x<0:
					return 0
				else:
					res+=x
			else:
				return 0
			break
	return res
			

print(fun([7,6,4,3,1]))