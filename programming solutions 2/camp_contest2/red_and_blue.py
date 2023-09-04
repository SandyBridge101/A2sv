t=int(input())

for _ in range(t):
    n=int(input())
    red=list(map(int,input().split()))
    m=int(input())
    blue=list(map(int,input().split()))
    #print(red,blue)
    mr=0
    mb=0
    mr=max(mr,red[0])
    mb=max(mb,blue[0])
    for i in range(1,n):
        red[i]+=red[i-1]
        mr=max(mr,red[i])
    
    for i in range(1,m):
        blue[i]+=blue[i-1]
        mb=max(mb,blue[i])
    print(mr+mb)