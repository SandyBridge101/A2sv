nums = [2,2,2,1,2,2,1,2,2,2]
k = 2

count={}
count['odd']=0
count['even']=0
l=0
cnt=0
n_sub=0
for r in range(0,len(nums)):
    
    if nums[r]%2!=0:
        count['odd']+=1
        cnt=0
    print(nums[l:r+1])

    
    while count['odd']==k:
        if nums[l]%2!=0:
            count['odd']-=1
        cnt+=1
        l+=1
    n_sub+=cnt

print(count,n_sub)