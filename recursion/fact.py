def factorial(n):
	#base case
	if n==1:#5
		return 1
	# sefl work
	return n * factorial(n-1)
'''
 1
 2 *1 =2
 3 * 2=6
4 * 6=24
 5 * 24=120


'''

print(factorial(5))