t=int(input())

for _ in range(t):
    n,m=list(map(int,input().split()))
    infected_houses=list(map(int,input().split()))
    infected=m
    infected_houses.sort()
    
    diff=[infected_houses[i]-infected_houses[i-1]-1 for i in range(1,m)]
    diff.append(infected_houses[0]-1 + n-infected_houses[-1])
    
    diff.sort()
    
    infected=0
    protected=0
    
    while diff and diff[-1]>infected:
        protected+=max(1,diff.pop()-1-infected)
        infected+=4
    
    print(n-protected)
    