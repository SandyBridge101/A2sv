def solve(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    for i in range(0,len(arr1)):
        if arr2[i]-arr1[i]<0 or arr2[i]-arr1[i]>1:
            return "NO"
    return "YES"

t=int(input())

for _ in range(t):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    print(solve(arr1,arr2))
