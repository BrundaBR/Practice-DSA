def binarysearch(nums,target):
	begin_idx=0
	end_idx=len(nums)-1
	while begin_idx<=end_idx:
		midpoint=begin_idx+(end_idx-begin_idx)//2
		midpoint_val=nums[midpoint]
		if midpoint_val==target:
			return midpoint
		elif target<midpoint_val:
			begin_idx=midpoint+1
			
		else:
			end_idx=midpoint-1
	return -1

def fun(nums,target):
    if len(nums)==1  and nums[0]!=target:
        return -1
    elif len(nums)==1 and nums[0]==target:
        return 0
    else:
    	begin_idx=0
    	end_idx=len(nums)-1
		while nums[begin_idx]<=nums[end_idx]:
			midpoint=begin_idx+(end_idx-begin_idx)//2
			midpoint_val=nums[midpoint]
			if nums[midpoint]>target:
				begin_idx=midpoint+1
			else:
				end_idx=midpoint-1
		nums=nums[begin_idx:end_idx]
		return binarysearch(nums,target)


nums=[1]
target=1
print(fun(nums,target))