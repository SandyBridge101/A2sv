N=int(input())

for _ in range(N):
    l=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    idx=set(arr)
    ch=''
    freq=[0 for i in range(0,max(arr)+1)]
    #print(idx,arr,freq)
    for i in range(0,len(arr)):
        freq[arr[i]]+=1
    #print(freq)
    
    for f in range(list(idx)[0],len(freq)-1):
        if freq[f]>=freq[f+1]:
            ch="YES"
        else:
            ch="NO"
            break
    if len(idx)==1 and list(idx)[0]>0:
        ch="NO"
    print(ch)