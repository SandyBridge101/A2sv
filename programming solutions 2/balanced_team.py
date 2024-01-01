from collections import *
def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    seen=defaultdict(int)
    m=1
    arr.sort()
    #print(arr)
    c=1
    l=0
    for i in range(0,n):
        if arr[i] not in seen:
            seen[arr[i]]=i
        
        for j in range(6):
            if arr[i]-j in seen:
                m=max(m,i-seen[arr[i]-j]+1)
                #print(i,seen[arr[i]-j])
                #print(arr[i],arr[i]-j,j)
    print(m)
    
solve()
