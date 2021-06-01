



output=[[]]
array=[1,2,3]
for num in array:
	output+=[curr+[num] for curr in output]
print(output)