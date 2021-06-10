## Dynamic Programming is mainly an optimization over plain recursion.




# Memoized solution

for example:
def fib(n,memo):
	if meme[n]!=null:
		return memo[n]
	if n==1 or n==2:
		result=1
	else:
		result=fib(n-1)+fib(n-2)
	memo[n]=result
	return result

complexity- o(n)

# bottom up approach
