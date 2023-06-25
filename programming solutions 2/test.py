t=int(input())

def eqn(x,y,k):
    return (2*x)+(k*y)

for i in range(0,t):
    inp=list(map(int,input().split()))
    n,k=inp[0],inp[1]
    cmp=0
    for y in range(0,n):
        N=0
        for x in range(0,n):
            N=eqn(x,y,k)
            #print((x,y),N)
            if N==n:
                cmp=N
                break
        if cmp==n:
            break
        
    if cmp==n:
        print("YES")
    else:
        print("NO")
