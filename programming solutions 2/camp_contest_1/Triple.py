from collections import Counter
t=int(input())

def solve():
    
    n=int(input())
    arr=list(map(int,input().split()))
    count={}
    
    
    for i in range(0,n):
        count[arr[i]]=1+count.get(arr[i],0)
        if count[arr[i]]>=3:
            return arr[i]
    

    return -1

for _ in range(t):
    print(solve())