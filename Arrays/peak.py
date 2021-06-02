def binarysearch(nums):
	begin_idx=0
	end_idx=len(nums)-1
	
	while begin_idx<end_idx:
		midpoint=(begin_idx+end_idx)//2
		if nums[midpoint] > nums[midpoint+1]:
			end_idx=midpoint
		else:
			begin_idx=midpoint+1 

	return end_idx

def base(nums):
	val=binarysearch(nums)
	return val

nums=[1,2,3,4,1]
print(base(nums))