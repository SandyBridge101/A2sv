t=int(input())

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    l=r=0
    neg=0
    while r<=n:
        if (r==n) or (arr[r]>0 and r!=0):
            if neg>0:
                #print(arr[l:r],neg)
                neg=0
                count+=1
                r+=1
                l=r

        if r<n and arr[r]<0:
            neg+=1
        r+=1
    sum=0
    for a in arr:
        sum+=abs(a)
    print(sum,count)

for _ in range(t):
    solve()
