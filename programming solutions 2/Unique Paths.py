class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}

        def dp(x,y):
            if x==m-1 and y==n-1:
                return 1
            if (x>=m or x<0) or (y>=n or y<0):
                return 0
            
            state=(x,y)

            if state not in memo:
                memo[state]=dp(x,y+1)+dp(x+1,y) 
            return memo[state]
        
        return dp(0,0)
