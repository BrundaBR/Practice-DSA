def fib(n):
	if n==0 or n==1:
		return 1
	# self work
	return fib(n-1)+fib(n-2)


print(fib(2))