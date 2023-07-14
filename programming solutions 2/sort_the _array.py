def check_order(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return 0
    return 1

def solve(arr,tmp,n):


    start=0
    end=0

    for i in range(0,n):
        if arr[i]!=tmp[i]:
            start=i
            break

    for i in range(n-1,-1,-1):
        if arr[i]!=tmp[i]:
            end=i
            break

    arr[start:end+1]=reversed(arr[start:end+1])

    if check_order(arr)==1:
        print("yes")
        print(start+1,end+1)
    else:
        print("no")

n=int(input())
arr=list(map(int,input().split()))
tmp=[i for i in arr]
tmp.sort()

solve(arr,tmp,n)

