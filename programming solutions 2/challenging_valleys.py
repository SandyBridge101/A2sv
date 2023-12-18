t=int(input())

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    l=0
    r=0
    count=0
    while r<n:
        if arr[l]==arr[r]:
            if l==0 or arr[l-1]>arr[l]:
                if r==n-1 or arr[r+1]>arr[r]:
                    count+=1
                    r+=1
                else:
                    r+=1
            else:
                r+=1
        else:
            l+=1
    #print(count)
    if count==1:
        return 'YES'
    else:
        return 'NO'
for _ in range(t):
    print(solve())
