class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        nums.append(0)

        memo={}
        

        if n<=3:
            return max(nums)

        def dp(i):
            if i==0:
                return nums[0]
            
            if i==1:
                return max(nums[1],nums[0])

            if i not in memo:
                memo[i]=max(dp(i-1),dp(i-2)+nums[i])

            return memo[i]
        
        temp=0
        nums[n-1],temp=temp,nums[n-1]
        a1=dp(n)
        nums[n-1],temp=temp,nums[n-1]

        nums[0]=0
        memo={}
        a2=dp(n)

        return max(a1,a2)
