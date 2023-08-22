from collections import Counter

s = "aabaabaa"
k = 1

count={}
res=0
p1=0

for p2 in range(0,len(s)):
    count[s[p2]]=1+count.get(s[p2],0)
    
    
    if (p2-p1+1)-max(count.values())>k:
        count[s[p1]]-=1
        p1+=1
    res=max(res,p2-p1+1)

print(res)