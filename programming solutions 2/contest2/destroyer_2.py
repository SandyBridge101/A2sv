N=int(input())

def solve():
    l=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    ch=''
    freq=[0 for i in range(0,max(arr)+1)]
    for i in range(0,len(arr)):
        freq[arr[i]]+=1
    #print(freq)
    for f in range(0,len(freq)-1):
        if freq[f]<freq[f+1]:
            return "NO"
            break
    return "YES"

for _ in range(N):
    print(solve())