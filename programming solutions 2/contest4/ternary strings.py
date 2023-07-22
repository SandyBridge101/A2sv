t=int(input())
for _ in range(t):
    s=list(map(int,list(input())))
    i=0
    tmp=[-1,-1,-1]
    ans=100000
    for i in range(len(s)):
        tmp[s[i]-1]=i
        if min(tmp)!=-1:
            ans=min(ans,max(tmp)-min(tmp)+1)
    if ans==100000: print(0)
    else: print(ans)