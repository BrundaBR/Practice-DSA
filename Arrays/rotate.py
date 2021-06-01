def rotate(nums,k):
	return nums[k+1:]+nums[0:k+1]


nums=[1,2,3,4,5,6,7,8,9]
k=3
print(rotate(nums,k))