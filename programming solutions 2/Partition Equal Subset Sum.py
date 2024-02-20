class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        n=len(nums)
        sm=sum(nums)
        

        if sm%2!=0:
            print(sm)
            return False

        target=sm//2

        def dp(i,total):
            if total==target:
                return True
            if total>target or i>=n:
                return False
            state=(total,i)
            if state not in memo:
              memo[state]= dp(i+1,total+nums[i]) or dp(i+1,total)
            return memo[state]
