

def solve():
    x=int(input())
    if x==1:
        return 3
    l=x.bit_length()
    #print(bin(x))
    res=[0]*(l)
    ans=0
    

    for i in range(0,l):
        b=int(x&(1<<i)!=0)
        #print(i,b,l)
        if b==1:
            res[i]=1
            ans^=(1<<i)
            break
    if i==l-1:
        res[0]=1
        ans^=(1<<0)

    return ans
    


    



for _ in range(int(input())):
    print(solve())
    
