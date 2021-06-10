'''
step1- sort array

step2- run loop next if next num is present

step3- if not retun next val



'''



def firstmissingpositive(nums):
	nums.sort()
	for i in range(len(nums)):
		val=nums[i]+1
		if nums[i+1]!=val:
			return val





nums=[3,4,-1,1]
print(firstmissingpositive(nums))