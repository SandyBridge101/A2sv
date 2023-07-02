N=int(input())

for _ in range(N):
    n=list(map(int,input().split()))
    arr=[list(input()) for i in range(0,n[0])]
    
    narr=[['.' for _ in range(0,len(arr[0]))] for _ in range(0,len(arr))]
    #print(arr)
    for r in range(0,len(arr)):
        for c in range(0,len(arr[0])):
            if str(arr[r][c])=='o':
                narr[r][c]='o'
                row,col=r,c
                x=1
                
                while arr[row][col]!='o' or row!=0:
                    if arr[row][col]=="*":
                        narr[r-x][c]="*"
                    row-=1
                
    print(narr)