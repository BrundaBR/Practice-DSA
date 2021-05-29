def recur(n):
	# print string in reverse order
	#basecase
	if len(n)>0:
		return n
	#subproblem
	
	for i in n:
		recur(i)
	#self work
	
	



if __name__ == '__main__':
	n=(input())
	print(recur(n))