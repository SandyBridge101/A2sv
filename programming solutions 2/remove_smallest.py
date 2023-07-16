def solve(arr,n):
    for i in range(0,n-1):
        diff=arr[i+1]-arr[i]
        if diff>1:
            return 'NO'
    return 'YES'


t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(solve(arr,n))