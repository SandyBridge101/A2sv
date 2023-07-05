N=int(input())

for _ in range(N):
    arr=list(map(int,input().split()))
    
    arr.sort()
    
    if arr[0]!=arr[1] and arr[2]!=arr[1]:
        arr[0]+=1
        arr[2]-=1
    elif arr[0]!=arr[1] and arr[2]==arr[1]:
        arr[2]-=1
        arr[1]-=1
        if len(set(arr))!=1:
            arr[0]+=1
    elif arr[0]==arr[1] and arr[2]!=arr[1]:
        arr[1]+=1
        arr[0]+=1
        if len(set(arr))!=1:
            arr[2]-=1
    sum=abs(arr[0]-arr[1])+abs(arr[2]-arr[0])+abs(arr[1]-arr[2])
    print(sum)