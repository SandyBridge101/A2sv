class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        if n==0 or n==1: return n
        print(nums)
        l=0
        m=0
        
        for i in range(1,len(nums)):

            if nums[i]-nums[i-1]!=1:
                l=i
            print(l,i)
            m=max(m,i-l+1)
        return m

            
