nums = [0,0,1,1,1,2,2,3,3,4]
n=len(nums)
unique=[]
unq=0
for i in range(0,len(nums)):
    if nums[i] in unique:
        nums[i]='_'
    else:
        unique.append(nums[i])

for i in nums:
    if i=='_':
        nums.remove(i)
        nums.append('_')
#nums=unique+[0 for i in range(0,n-len(unique))]
print(nums,unique)