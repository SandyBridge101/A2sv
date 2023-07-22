nums = [1,2,3,4,5,6,7]
k = 3
start=0
end=len(nums)-1
for _ in range(0,k):
    nums.insert(start,nums[end])
    nums.pop()
print(nums)