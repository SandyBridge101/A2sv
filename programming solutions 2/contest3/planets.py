from collections import Counter
t=int(input())

for _ in range(t):
    n,c=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    arr=Counter(arr)
    arr=dict(arr)
    #print(n,c,arr)
    
    sum=0
    for i in arr:
        
        #print(i,arr[i])
        if arr[i]==1:
            sum+=arr[i]
        else:
            if c>arr[i]*1:
                sum+=arr[i]
            else:
                sum+=c

    print(sum)