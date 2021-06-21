'''

Iterate through each entry in an array, A.

Track the furthest we can reach from entry (A[i] + i)

If for some i, we don’t reach the end and that is the furthest we can reach, then we can’t reach the last index. Otherwise, the end is reached.

i: index processed. Furthest possible to advance from i: A[i] + i
'''

def arraygame(a):
	furthest= 0
	i=0
	n=len(a)
	while i<n and furthest<n:
		furthest=max(furthest,a[i]+i)
		i+=1
	if furthest>=n-1:
		return True
	else:
		return False



a=[3,3,1,0,2,0,1]
print(arraygame(a))