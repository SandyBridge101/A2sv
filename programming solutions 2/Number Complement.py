class Solution:
    def findComplement(self, num: int) -> int:
        
        bit=[]

        while num>0:
            if num%2==0:
                bit.append(1)
            else:
                bit.append(0)
            num=num//2
        
        x=0
        c=0
        for n in bit:
            c+=((2**x)*n)
            x+=1


        print(bit,c)
        return c

