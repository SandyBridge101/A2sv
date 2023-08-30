nums=[1,2,3]
k=3
count=0
ps=[0]*(len(nums))
dic={}
ps[0]=nums[0]
dic[0]=nums[0]

for i in range(1,len(nums)):
    ps[i]=nums[i]+ps[i-1]
    print(dic,ps[i],k,ps[i]-k)
    if ps[i]==k:
        count+=1
    if ps[i]-k in dic.values():
        count+=1
    
    dic[i]=ps[i]



print(ps,dic,count)