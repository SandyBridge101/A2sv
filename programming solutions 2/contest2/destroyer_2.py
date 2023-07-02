N=int(input())

for _ in range(N):
    l=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    old_count=len([i for i in arr if i==0])
    ch=""
    
    for i in range(1,max(arr)):
        if arr[0]!=0:
            ch="NO"
            break
        new_count=len([k for k in arr if k==i])
        if new_count+1==old_count or new_count==old_count:
            ch="YES"
        else:
            ch="NO"
            
    print(ch)