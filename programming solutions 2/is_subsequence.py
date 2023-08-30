class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0

        for i in range(0,len(t)):
            if p>=len(s):break
            if t[i]==s[p]:
                
                p+=1

        return p==len(s)