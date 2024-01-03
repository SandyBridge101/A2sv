def solve():
    a=input()
    b=input()


    def equivalent(a):
        if len(a)%2:
            return a
        m=len(a)//2

        x,y=equivalent(a[:m]),equivalent(a[m:])
        if x<y:
            return x+y
        else:
            return y+x


    if equivalent(a)==equivalent(b):
        return 'YES'
    else:
        return 'NO'


print(solve())


