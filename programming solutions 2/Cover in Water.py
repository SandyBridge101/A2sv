 
def solve():
    n=int(input())
    s=input()
    c=0
    t=0
 
    for i in s:
        if c==3:
            return 2
        if i=='.':
            c+=1
            t+=1
        else:
            c=0
    if c==3:
        return 2
        
    return t
 
 
for _ in range(int(input())):
    print(solve())
