t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    max_sum=arr[0]
    sm=0
    for i in range(n):
        if (arr[i]*max_sum<0):
            sm+=max_sum
            max_sum=arr[i]
        else:
            max_sum=max(max_sum,arr[i])
        
    print(sm+max_sum)