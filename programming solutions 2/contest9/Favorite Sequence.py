t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    p1=0
    p2=n-1
    narr=[0 for i in arr]
    x=0

    while p2-p1>=0:
        #print(p1,p2,arr[p1],arr[p2],narr)
        if p2==p1:
            narr[x]=arr[p1]
            x+=1
            p1+=1
            break
        narr[x]=arr[p1]
        x+=1
        p1+=1
        narr[x]=arr[p2]
        x+=1
        p2-=1

    print(*narr)