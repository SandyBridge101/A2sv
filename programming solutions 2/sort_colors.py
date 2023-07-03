nums = [2,0,2,1,1,0]

for i in range(0,len(nums)):
    for j in range(0,len(nums)-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)