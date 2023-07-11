

def solve(arr,mx,mx2):
    results=[]
    for x in range(0,len(arr)):
        if arr[x]==mx:
            results.append(arr[x]-mx2)
        else:
            results.append(arr[x]-mx)
    return results

t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    tmp_arr=[i for i in arr]
    tmp_arr.sort()
    mx=tmp_arr[n-1]
    mx2=tmp_arr[len(arr)-2]
    #print(mx,mx2)
    print(*solve(arr,mx,mx2))