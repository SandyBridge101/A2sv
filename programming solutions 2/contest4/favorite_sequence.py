t=int(input())

for _ in range(t):
    n=int(input())
    sequence=list(map(int,input().split()))
    arr=[]
    
    start=0
    end=n-1
    
    while start<=end:
        if start==end:
            arr.append(sequence[start])
            break
        arr.append(sequence[start])
        arr.append(sequence[end])
        start+=1
        end-=1

    print(*arr)