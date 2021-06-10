'''
step1- two pointers run over the array

step2- create var profit 

step3-if price[j]>price[i]: 
		if price[j]-price[i]>profit:
			then replace profit

step 4- return profit

Dry run:

		
'''
def buysell(p):
	profit=0
	n=len(p)
	i=0
	while  i < n-1:
		for j in range(i+1,n):
			val=p[j]-p[i]
			if val>profit:
				profit=val
		i+=1


	return profit











prices= [7,6,4,3,1]
print(buysell(prices))