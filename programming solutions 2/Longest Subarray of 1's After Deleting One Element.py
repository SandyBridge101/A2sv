nums = [1,1,1]

count={}
count[1]=0
mxl=0
left=0
for right in range(0,len(nums)):
    count[nums[right]]=1+count.get(nums[right],0)
    n=(right-left)+1
    
    if n-count[1]>1:
        count[nums[left]]-=1
        left+=1
        
    else:
        print(count,left,right,mxl,nums[left:right+1])
        mxl=max((right-left)+1,mxl)

print(mxl-1)