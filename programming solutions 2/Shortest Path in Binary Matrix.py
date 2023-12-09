class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        color=[[-1]*(m) for i in range(n)]
        direction=[[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        start=[0,0,1]
        end=[n-1,m-1]

        def bfs(node):
            queue=deque()
            queue.append(node)

            while queue:
                curr=queue.popleft()
                if grid[curr[0]][curr[1]]==0 and curr[0]==end[0] and curr[1]==end[1]:
                    return curr[2]

                for d in direction:
                    r,c,l=curr[0]+d[0],curr[1]+d[1],curr[2]+1
                    if (r<n and r>=0) and (c<m and c>=0):
                        if grid[r][c]==0 and color[r][c]==-1:
                            queue.append([r,c,l])
                            color[r][c]=0
                #print(queue)
            #print(curr)
            return -1

        color[0][0]=0
        if grid[0][0]==0:
            return bfs(start)
        else:
            return -1
