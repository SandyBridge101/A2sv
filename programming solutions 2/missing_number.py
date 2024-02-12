class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=set(nums)
        
        for i in range(-1,n):
            x=i+1
            if x not in s:
                return x
