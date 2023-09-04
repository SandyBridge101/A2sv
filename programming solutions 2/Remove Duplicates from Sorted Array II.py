nums=[0,0,1,1,1,1,2,3,3]

n=len(nums)
count={}
unique=0
for i in range(n):
    count[nums[i]]=1+count.get(nums[i],0)
    if count[nums[i]]>2:
        nums[i]=float('inf')
    else:
        unique+=1
nums.sort()
print(count,nums,unique)