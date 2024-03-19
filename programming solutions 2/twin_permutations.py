
def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    res=[]

    k=n+1

    for i in range(n):
        res.append(abs(arr[i]-k))
    return res


for _ in range(int(input())):
    print(*solve())
