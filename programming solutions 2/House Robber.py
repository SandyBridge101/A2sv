class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        nums.append(0)
        memo={}

        def dp(num):
            if num==0:
                return nums[num]

            if num==1:
                return max(nums[0],nums[1])
                

            if num not in memo: 
                memo[num]=max(dp(num-1),dp(num-2)+nums[num])
            return memo[num]

        return dp(n)
