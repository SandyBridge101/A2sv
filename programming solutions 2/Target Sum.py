class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}

        def dp(i,amount):
            if amount==0 and i>=n:
                return 1
            if i>=n and amount!=0:
                return 0

            state=(i,amount)

            if state not in memo:
                memo[state]=dp(i+1,amount-nums[i]) + dp(i+1,amount+nums[i])
            
            return memo[state]

        return dp(0,target)
