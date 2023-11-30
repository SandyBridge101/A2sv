class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x,y=len(image),len(image[0])
        direction=[[0,1],[1,0],[-1,0],[0,-1]]
        initial_color=image[sr][sc]
        
        def dfs(row,col):
        
            if image[row][col]!=initial_color or image[row][col]==color:
                return
            image[row][col]=color
            for d in direction:
                r,c=row+d[0],col+d[1]
                if r>=0 and c>=0 and r<x and c<y:
                    dfs(r,c)
        
        dfs(sr,sc)
        return image
        
