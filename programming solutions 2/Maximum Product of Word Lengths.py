class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        mx=-1
        def check(a,b):
            for k in range(26):
                if d[i][k] & d[j][k]==1:
                    return False
            
            return True

        print(ord('a'),ord('z'))#-97

        d=[[0]*(26) for _ in words]

        for i in range(n):
            for l in words[i]:
                d[i][ord(l)-97]=1


        for i in range(n):
            li=len(words[i])
            for j in range(i+1,n):
                lj=len(words[j])
                if check(d[i],d[j]):
                    p=li*lj
                    #print(words[i],words[j],p)
                    mx=max(mx,p)

        if mx==-1:mx=0
        return mx
