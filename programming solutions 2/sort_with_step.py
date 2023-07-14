t=int(input())

for _ in range(t):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    count=0
    for i in range(0,n):
        if (arr[i]-i-1)%k==0:
            continue
        count+=1
    if count==0:print(0)
    elif count<=2:print(1)
    else:print(-1)
    