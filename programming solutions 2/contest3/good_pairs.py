def solve(arr):
    min_val=min(arr)
    max_val=max(arr)
    min_index=arr.index(min_val)
    max_index=arr.index(max_val)
    
    if min_val==max_val:
        return min_index,max_index
    if min_index<max_index:
        return min_index,max_index
    else:
        return max_index,min_index

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    i,j=solve(arr)
    print(i+1,j+1)