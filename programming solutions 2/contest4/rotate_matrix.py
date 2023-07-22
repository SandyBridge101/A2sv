t=int(input())
for _ in range(t):
    r1=list(map(int,input().split()))
    r2=list(map(int,input().split()))
    mat=[r1,r2]
    #print(mat)
    
    if (mat[0][0]<mat[0][1] and mat[1][0]<mat[1][1] or mat[0][0]>mat[0][1] and mat[1][0]>mat[1][1]) and (mat[0][0]<mat[1][0] and mat[0][1]<mat[1][1] or mat[0][0]>mat[1][0] and mat[0][1]>mat[1][1]):
        print('YES')
    else:
        print('NO')