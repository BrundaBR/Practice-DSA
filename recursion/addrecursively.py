def addnumbers(n):
	#base case
	if n==1:
		return 1
	#recurive call
	subproblem=addnumbers(n-1)

	#self work
	return n+subproblem



print(addnumbers(2))