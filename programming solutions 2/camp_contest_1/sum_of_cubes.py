t=int(input())
cubes={i*i*i for i in range(1,10001)}
def solve():
    N=int(input())
    #print(N)
    i=1
    while i*i*i<=N:
        j=N-(i*i*i)
        if j in cubes:
            return 'YES'
        i+=1
    return'NO'

for _ in range(t):
    print(solve())

