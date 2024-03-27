class Solution:
    def longestPrefix(self, s: str) -> str:
        m=10**15+7
        def mul(a,b):
            return ((a%m)*(b%m))%m
        n=len(s)
        rs=s[::-1]
        a=27
        alph={chr(i+97):i+1 for i in range(26)}
        seen=set()
        #print(alph)
        l=n-1
        phsh=0
        shsh=0
        p=-1
        for r in range(n):
            phsh=((phsh%m)+(alph[s[r]]%m))%m
            seen.add(phsh)
            #print(phsh,s[r])
            phsh=mul(phsh,a)%m

        #print(seen)
        b=1
        for r in range(n-1):
            shsh=((mul(((b)%m),(alph[rs[r]]%m))%m)+(shsh%m))%m
            #print(shsh,rs[r],r)
            if shsh in seen:
                p=r
            b=(a*b)%m

        
        res=s[n-(p+1):n]

        return res


        

        