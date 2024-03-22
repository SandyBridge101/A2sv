

def solve():
    n=int(input())
    arr=list(map(int,input().split()))
    s=n
    v=0
    z=0
    for i in range(n):
        if arr[i]!=0:
            s=i
            break
    #print('--',s)
    for i in range(s,n-1):
        if arr[i]==0:
            z+=1
        else:
            v+=arr[i]

    return v+z



for _ in range(int(input())):
    print(solve())
