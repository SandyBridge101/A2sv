class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        n=len(ranges)
        ranges.sort()

        count=1
        p_end=-1
        k=1_000_000_007

        #if n==1: return 2
        for i in range(0,n):
            low=ranges[i][0]
            hi=ranges[i][1]
            if low>p_end:
                count=count*2%k
            p_end=max(p_end,hi)

        print(ranges)

        return count
