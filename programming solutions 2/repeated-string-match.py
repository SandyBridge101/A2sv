class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n=len(b)
        m=len(a)
        s=a
        l=m
        for _ in range(n):
            s+=a
            l+=m
            if l>2*n:
                break

        print(b,s,l,len(s),m)

        def find(s,x,p):
            l=len(s)
            s=x+'#'+s
            n=len(s)
            m=len(x)
            lps=[0]*(n)
            lps = [0] * n
            count = 0

            for i in range(1, n):
                j = lps[i-1]
                
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                
                if s[i] == s[j]:
                    j += 1
                
                if j == m:
                    #print(lps)
                    #print(i-m,s[i-m])
                    return i-m
                    
                lps[i] = j

            return -1
            



        index=find(s,b,m)

        if index==-1: return index
        
        print(index,s[index])


        for j in range(index,len(s)+1):
            if j%m==0:
                print(j)
                return j//m




        return 0