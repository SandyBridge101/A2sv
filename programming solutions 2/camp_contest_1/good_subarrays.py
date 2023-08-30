t=int(input())

def solve():
    
    n=int(input())
    nums=list(map(int,input()))
    print(nums)
    sum=0
    l=0
    count=0
    for r in range(0,len(nums)):
        sum=nums[r]+sum
        l=0
        nsum=sum
        while r!=l:
            print(r,l,nsum,(r-l)+1)
            if nsum==(r-l)+1:
                count+=1
            nsum-=nums[l]
            l+=1
    return nums,count

for _ in range(t):
    print(solve())