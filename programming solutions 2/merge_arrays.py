
n,m=map(int,input().split())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
result=[]
N=max(m,n)
p1=0
p2=0
while p1<n and p2<m:
    if arr1[p1]<arr2[p2]:
        result.append(arr1[p1])
        p1+=1
    else:
        result.append(arr2[p2])
        p2+=1
if p1==n:result.extend(arr2[p2:])
if p2==m:result.extend(arr1[p1:])
print(*result)