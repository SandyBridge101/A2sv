class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1=grid[0].copy()
        row2=grid[1].copy()
        n=len(grid[0])

        for i in range(1,n):
            row1[i]+=row1[i-1]
            row2[i]+=row2[i-1]

        ans=row1[-1] - row1[0]

        for i in range(1,n):
            b=row2[i-1] if i>0 else 0
            a=row1[-1]-row1[i]
            mx=max(a,b)
            ans=min(ans,mx)
            #print(curr_junc,end=" ")


        return ans
