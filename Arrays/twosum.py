def twosum(nums,t):
	dict={}
	for i in range(len(nums)):
		dict[i]=nums[i]
	

	for i in range(len(nums)):
		complement=t-nums[i]
		for key,value in dict.items():
			if value==complement and i!=key:
				return [i,key]



nums=[3,2,3]
t=6
print(twosum(nums,t))