nums = [8,1,2,2,3]
result=[]

for i in range(0,len(nums)):
    count=0
    for j in range(0,len(nums)):
        if i==j:
            continue
        else:
            if nums[i]>nums[j]:
                count+=1
    result.append(count)
    
print(result)