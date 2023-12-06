class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        color=[[0]*(len(grid[0])) for g in grid]
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        n=0
        def dfs(row,col,arr):
            if (grid[row][col]==0) or (color[row][col]==-1):
                return 
            color[row][col]=-1
            arr.append(grid[row][col])
            for d in direction:
                r,c=row+d[0],col+d[1]
                if (r>=0 and r<len(grid)) and (c>=0 and c<len(grid[0])):
                    dfs(r,c,arr)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if color[r][c]==0 and grid[r][c]==1:
                    n+=1
                    area=[]
                    dfs(r,c,area)
                    max_area=max(max_area,sum(area))

        
        return max_area
