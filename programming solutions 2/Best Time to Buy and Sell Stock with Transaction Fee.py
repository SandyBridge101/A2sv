class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)


        profit=0
        hold=profit-prices[0]


        for i in range(1,n):

            hold=max(hold,profit-prices[i])
            profit=max(profit,hold+prices[i]-fee)

        return profit

    
            
        return max(dp)
