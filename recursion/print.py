def printing(n):
	#base case
	if n==0: # 5
		return n+1
	#recursive call
	
	print(printing(n-1))
	return n+1



'''
output: 5  4  3 2  1 
'''
printing(5)