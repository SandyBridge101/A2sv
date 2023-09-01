class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        total=sum(beans)
        beans.sort()
        n=len(beans)
        ans=total
        if n==1: return 0
        for i in range(0,n):
            ans=min(ans,total-((n-i)*beans[i]))
        return ans
