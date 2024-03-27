class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        diff=[0]+[0]*(n)+[0]
        res=[0]*(n)
        ans=''
    
        for l,r,m in shifts:
            k=0
            if m==1:
                k=1
            else:
                k=-1

            diff[l+1]+=k
            diff[r+2]-=k

        #print(diff,res)

        for i in range(1,n+2):
            diff[i]+=diff[i-1]
        
        x=0
        for i in range(1,n+1):
            res[x]=(diff[i]+(ord(s[x])-97))%26
            x+=1

        for r in res:

            ans+=chr(r+97)



        return ans
        