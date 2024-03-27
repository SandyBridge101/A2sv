class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n=len(s)
        s=s[::-1]
        p=pow(power,k-1,modulo)

        def val(x):
            return ord(x)-96

        hsh=0
        res=0

        for i in range(k):
            hsh=((hsh*power)+val(s[i]))%modulo
        
        if hsh==hashValue:
            res= s[:k][::-1]

        for i in range(k,n):
            hsh=(hsh - (val(s[i-k])*(p) )) %modulo
            hsh=((hsh*power)+val(s[i]))%modulo

            if hsh==hashValue:
                res= s[i-k+1:i+1][::-1]

        return res




        