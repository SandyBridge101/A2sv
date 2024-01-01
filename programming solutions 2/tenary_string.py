from collections import *

t=int(input())

def solve():
    arr=input()
    m=200005
    n=len(arr)
    l=0
    r=0
    count=defaultdict(int)
    
    for r in range(n):
        count[arr[r]]+=1
        if count['1']>0 and count['2']>0 and count['3']>0:
            while count['1']>0 and count['2']>0 and count['3']>0:
                m=min(m,r-l+1)
                count[arr[l]]-=1
                l+=1
            
    if m==200005:
        return 0
    return m
        
for _ in range(t):
    print(solve())
