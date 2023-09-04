def perform_operation(l,r,d):
    for i in range(l-1,r):
        arr[i]+=d

def perform_query(x,y):
    q=[]
    for i in range(n):
        q.append(matrix[y][i]-matrix[x-1][i])
    
    return q



n,m,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
matrix=[]
matrix.append(arr.copy())
operation_set=[None]*(m)
queries=[]
for i in range(m):
    operation_set[i]=list(map(int,input().split()))
    perform_operation(operation_set[i][0],operation_set[i][1],operation_set[i][2])
    matrix.append(arr.copy())

for i in range(k):
    x,y=list(map(int,input().split()))
    queries.append(perform_query(x,y))


#print(queries)
res=matrix[0]
for i in range(n):
    s=0
    for j in range(k):
        s+=queries[j][i]
    res[i]+=s
print(*res)
