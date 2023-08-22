target = 7
nums = [2,3,1,2,4,3]
p1=0
p2=0
min_range=len(nums)+1
curr_sum=0
max_sum=0
min_range=len(nums)+1

while p2<len(nums):
    curr_sum+=nums[p2]
    while p1<p2 and curr_sum>=target:
        min_range=min(min_range,(p2-p1)+1)
        max_sum=max(max_sum,curr_sum)
        #print(min_range,p2,p1)
        curr_sum-=nums[p1]
        p1+=1
    p2+=1
if max_sum>=target:
    print(min_range)
else:
    print(0)