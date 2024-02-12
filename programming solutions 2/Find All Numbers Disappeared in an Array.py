class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s=[-1 for _ in range(n)]
        ans=[]
        for i in range(0,len(nums)):
            s[nums[i]-1]=nums[i]

        return [i+1 for i in range(n) if s[i]==-1]
        
