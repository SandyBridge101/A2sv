#arr=[1,1,3,2,1]
arr=list(map(int,input().split()))
m=max(arr)
mn=min(arr)
if mn==0:m+=1
print(m,mn,len(arr))
freq=[0 for i in range(0,m+1)]
result=[]
for i in range(0,len(arr)):
    freq[arr[i]]+=1


print(freq)