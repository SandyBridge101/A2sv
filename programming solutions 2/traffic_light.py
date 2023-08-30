t=int(input())

def solve():
    n,k=input().split()
    nums=list(input())
    nums+=nums
    p=len(nums)
    mxt=0

    for i in range(len(nums)-1,-1,-1):
        if nums[i]=='g':
            p=i
        if nums[i]==k:
            mxt=max(mxt,p-i)
    return mxt

for _ in range(t):
    print(solve())
