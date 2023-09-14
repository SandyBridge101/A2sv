class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_gulps(x,piles):
            count=0
            for i in piles:
                count+=ceil(i/x)
            return count
        print(count_gulps(4,piles))

        low,high=1,max(piles)
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            if count_gulps(mid,piles)<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1


        return ans
        
