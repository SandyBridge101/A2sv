class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[-1 for _ in range(n)]
        ans=[]

        for k in nums:
            if s[k-1]==k:
                ans.append(k)
            else:
                s[k-1]=k
        #print(s) 
        for i in range(n):
            if s[i]==-1:
                ans.append(i+1)

        return ans
