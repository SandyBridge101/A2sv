from collections import Counter

def is_equal(arr1,arr2):
    count={}
    
    for i in arr1:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
            
    for i in arr2:
        if i not in count or count[i]==0:
            return False
        else:
            count[i]-=1
    
    return True

s = "cbaebabacd"
p = "abc"
n=len(p)-1

cp=Counter(p)
cs=Counter(s[0:n])


res=[]


for p2 in range(n,len(s)):
    p1=p2-n
    cs[s[p2]]+=1
    print(s[p1:p2+1],p,cs,cs==cp)
    if cs==cp:
        res.append(p1)
    cs[s[p1]]-=1

print(res)