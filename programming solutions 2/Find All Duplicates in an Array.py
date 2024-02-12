class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=max(nums)
        s=[-1 for i in range(n)]
        ans=[]


        for k in nums:
            if s[k-1]==k:
                ans.append(k)
            else:
                s[k-1]=k

        return ans
            
        
