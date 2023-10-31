def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    l=0
    r=0
    num=1
    while num<2*(10**5):
        num+=1
print(solve())
