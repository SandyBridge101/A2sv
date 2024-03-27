class Solution:
    def longestPrefix(self, s: str) -> str:
        s=s[:len(s)-1]+'#'+s
        n=len(s)
        lps=[0]*(n)

        for i in range(1,n):
            j=lps[i-1]

            while j>0 and s[i]!=s[j]:
                j=lps[j-1]
            
            if s[i]==s[j]:
                j+=1

            lps[i]=j

        print(lps)
        x=lps[-1]
        return s[:x]




        

        