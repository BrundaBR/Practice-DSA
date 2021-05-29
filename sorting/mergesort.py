'''
split
divide 
merge and sort


'''
def mergesort(t):
	#base case

	if len(t)>1:
		#subproblem
		mid=len(t)//2
		left=t[:mid]
		right=t[mid:]
		mergesort(left)
		mergesort(right)
		i=0
		j=0
		k=0
		#comparing the value
		while i<len(left) and j<len(right):
			if left[i]<right[j]:
				t[k]=left[i]
				i=i+1
				k=k+1
			else:
				t[k]=right[j]
				j=j+1
				k=k+1	
		#while the values are left add to the list 	
		while len(left)>i:
			t[k]=left[i]
			i=i+1
			k=k+1
		while len(right)>j:
			t[k]=right[j]
			j=j+1
			k=k+1


test=[18,9,0,3,5,6,7]
mergesort(test)
print(test)