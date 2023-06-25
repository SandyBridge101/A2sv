N=int(input())

nums=list(map(int,input().split()))

nums_sum=sum(nums)

averages=[]

#print(nums_sum)

for i in range(0,N):
    #print(i)
    avg=(nums_sum-nums[i])/(N-1)
    if nums[i]==avg:
        #print(i+1)
        averages.append(i+1)
print(len(averages))
print(*averages)