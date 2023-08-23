t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    #print(n)
    arr.sort()
    left=0
    right=n-1
    cost=0
    while right>left:
        cost+=arr[right]-arr[left]
        right-=1
        left+=1
    print(cost)