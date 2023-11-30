class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x=len(grid[0])
        y=len(grid)
        color=[[-1]*(x) for i in range(y)]

        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        
        cord=[2,3]

        def dfs(row,col):
            if color[row][col]==0 or grid[row][col]=="0":
                return
            color[row][col]=0

            for dir in direction:
                r,c=row+dir[0],col+dir[1]
                if (r<y and r>=0) and (c>=0 and c<x):
                    dfs(r,c)   
            return
        
        count=0
        for i in range(y):
            for j in range(x):
                if (i<y and i>=0) and (j>=0 and j<x):
                    if grid[i][j]=="1" and color[i][j]==-1:
                        count+=1
                        dfs(i,j)
