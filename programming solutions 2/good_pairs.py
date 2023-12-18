from collections import *
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
diff=[]
for k in range(n):
    diff.append(a[k]-b[k])
#print(diff)
diff.sort()
l=0
r=n-1
count=0

while l<r:
    #print(l,r)
    if diff[l]+diff[r]>0:
        count+=(r-l)
        r-=1
    else:
        l+=1

print(count)
