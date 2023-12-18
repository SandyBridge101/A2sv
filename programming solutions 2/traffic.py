t=int(input())

def solve():
    n,k=input().split()
    n=int(n)
    nums=list(input())
    nums+=nums
    mx=0
    l=-1
    r=0
    while r<2*n:
        if nums[r]==k and l==-1:
            l=r
        if nums[r]=='g' and l!=-1:
            mx=max(mx,r-l)
            #print(nums[l:r],r-l)
            l=-1
        r+=1
    print(mx)
for _ in range(t):
    solve()
