def bubble(li):
	sort=False
	l=len(li)-1
	while not sort:
		sort=True
		for i in range(l):
			if li[i] > li[i+1]:
				sort=False
				li[i],li[i+1]=li[i+1],li[i]
				
	return li
print(bubble([3,4,6,21,0]))