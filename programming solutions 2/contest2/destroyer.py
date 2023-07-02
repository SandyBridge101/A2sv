N=int(input())

for _ in range(N):
    l=int(input())
    arr=list(map(int,input().split()))
    #print(arr)
    if arr[0]==0:
        ch=""
        for i in range(0,l-1):
            if arr[i+1]-arr[i]<=1:
                ch="YES"
                if arr[i+1]-arr[i]<0:
                    if arr[i+1]==0:
                        ch="YES"
                    else:
                        ch="NO"
                        break
            else:
                ch="NO"
                break
        print(ch)
    else:
        print("NO")