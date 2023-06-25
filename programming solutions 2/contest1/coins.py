t=int(input())


def find_xy(n,k):
    x=0
    y=0
    while 2*x<=n:
        if (n-(2*x))%k==0:
            y=(n-(2*x))//k
            break
        x+=1
    if (2*x)+(k*y)==n:
        return "YES"
    else:
        return "NO"

for i in range(0,t):
    inp=list(map(int,input().split()))
    n,k=inp[0],inp[1]
    
    if  n>=k and n%2==0 or (n-k)%2==0 or n%k==0:
        print("YES")
    else:
        print("NO")