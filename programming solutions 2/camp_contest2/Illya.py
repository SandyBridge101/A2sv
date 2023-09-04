s=input()
t=int(input())
n=len(s)
ps=[0]*n
for i in range(1,n):
    if s[i]==s[i-1]:
        ps[i]=ps[i-1]+1
    else:
        ps[i]=ps[i-1]

for _ in range(t):
    l,r=list(map(int,input().split()))
    res=ps[r-1]-ps[l-1]
    if res>0:
        print(res)
    else:
        print(0)