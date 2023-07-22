nums = [111311, 1113]
n=len(nums)
nums=[str(num) for num in nums]
tmp=[]
for i in range(0,n):
    for j in range(0,n-1):
        if int(nums[j]+nums[j+1])<int(nums[j+1]+nums[j]):
            nums[j],nums[j+1]=nums[j+1],nums[j]
            
"""    tmp=int(''.join([str(i) for i in nums]))
    max_num=max(max_num,tmp)
    print(tmp,max_num)"""


print(''.join([str(i) for i in nums]))