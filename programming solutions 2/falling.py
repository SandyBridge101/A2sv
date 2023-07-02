N=int(input())

for _ in range(N):
    n=list(map(int,input().split()))
    arr=[list(input()) for i in range(0,n[0])]
    narr=[['.' for _ in range(0,len(arr[0]))] for _ in range(0,len(arr))]
    for i in range(0,len(arr)):
            for r in range(len(arr)-1,-1,-1):
                for c in range(0,len(arr[0])):
                    if arr[r][c]=='.' and arr[r-1][c]=='*':
                        if r!=0 and arr[r][c]!='o':
                            arr[r][c],arr[r-1][c]=arr[r-1][c],arr[r][c]
                        else:
                            continue
    for r in range(0,len(arr)):
        print(''.join(arr[r]))
    print('\n')

