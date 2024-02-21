class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        coins.sort(reverse=True)

        def dp(amount,count):
        
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            if amount in memo:
                return memo[amount]
        
            count+=1
            res=float('inf')

            for c in coins:
                res=min(res,1+dp(amount-c,count))

            memo[amount]=res
            
            return memo[amount]
        
        ans=dp(amount,0)
        
        if ans==float('inf'):
            return -1
        else:
            return ans
