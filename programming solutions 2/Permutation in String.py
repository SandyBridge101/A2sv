from collections import Counter
s1 = "ab"
s2 = "eidbaooo"

n=len(s1)-1
cs1=Counter(s1)
cs2=Counter(s2[0:n])

for p2 in range(n,len(s2)):
    p1=p2-n
    cs2[s2[p2]]+=1
    print(s1,s2[p1:p2+1],cs2)
    if cs2==cs1: print(True)
    cs2[s2[p1]]-=1
