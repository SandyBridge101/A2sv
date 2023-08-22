from collections import Counter

n,k=list(map(int,input().split()))
arr=input()
p1=0
p2=0
l=0
count={}
for p2 in range(0,len(arr)):
    count[arr[p2]]=1+count.get(arr[p2],0)
    
    
    if (p2-p1+1)-max(count.values())>k:
        count[arr[p1]]-=1
        p1+=1
    l=max(l,p2-p1+1)


print(l)