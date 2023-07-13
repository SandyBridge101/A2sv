n=int(input())
arr=list(map(int,input().split()))

even=[i for i in arr if i%2==0]
odd=[i for i in arr if i%2!=0]


if len(even)>0 and len(odd)>0:
    arr.sort()

print(*arr)

