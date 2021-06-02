'''
Binary search -0(nlogn) time complexity

'''


def binarysearch(nums,target):
	begin_idx=0
	end_idx=len(nums)-1
	while begin_idx<=end_idx:
		midpoint=begin_idx+(end_idx-begin_idx)//2
		
		midpoint_val=nums[midpoint]
		if midpoint_val==target:
			return midpoint
		elif target<midpoint:
			end_idx=midpoint-1
		else:
			begin_idx=midpoint+1


nums=[1,2,3,4,5,6,7,8,9]
target=8
print(binarysearch(nums,target))