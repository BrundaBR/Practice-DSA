
'''
pseudocode


step 1: for loop from 0 to n-1  --

step2: while loop from i+1 to n-1 --

step3: store visited indexed in prev list --

step4:for each iteration multiply  ---
product(prev) and product

step 5: final_product should be added to 
result list
step 6: special case for last element 
id to multiply list append to result

to calculate a product

from operator import mul
>>> reduce(mul, [1, 2, 3], 1)



'''
import itertools
def mul(x):
	prod=1
	for i in x:
		prod*=i
	return prod

def sumofarray(a):
	product=1 #2
	result=[]
	prev=[]  #1
	final_product=1
	j=1
	for i in range(len(a)):  #1
		prev.append(a[i])
		while j < len(a): # 1<5
			product*=a[j]  
			 # 2 * 3 =6
			if j==len(a)-1:
				x=mul(prev)
				result.append(x)
				break
			else:
				j+=1

		if len(prev)!=0:
			x=mul(prev)
			y=product*x
			final_product*=y
			result.append(final_product)
			print(final_product)
			product=1
			final_product=1
		else:
			result.append(product)
			product=1
	
	return result



# arr=list(map(int,input().split(',')))  [24,12,8,6]
arr=[1,2,3,4]
print(sumofarray(arr))