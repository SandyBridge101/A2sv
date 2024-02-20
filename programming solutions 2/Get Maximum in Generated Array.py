class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0]*(n+1)
        if n<2:
            return n
        nums[0]=0
        nums[1]=1

        memo={}

        def dp(i):
            if i ==1 or i==0:
                return i

            x,y=i//2,i%2
            
            if y==1:
                nums[i]=dp(x)+dp(x+1)
            else:
                nums[i]=dp(x)

            if i not in memo:
                memo[i]=nums[i]
            return memo[i]

        for k in range(n+1):
            dp(k)
        print(nums)

        return max(nums)
