class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m,n=len(mat[0]),len(mat)
        direction=[[0,1],[1,0],[0,-1],[-1,0]]

        def bfs():
            queue=deque()
            for r in range(n):
                for c in range(m):
                    if mat[r][c]==0:
                        queue.append([r,c])
                    else:
                        mat[r][c]=m*n

            while queue:
                curr=queue.popleft()
                for d in direction:
                    r,c=curr[0]+d[0],curr[1]+d[1]
                    if (r>=0 and r<n) and (c>=0 and c<m) and mat[r][c]>mat[curr[0]][curr[1]]:
                        queue.append([r,c])
                        mat[r][c]=mat[curr[0]][curr[1]]+1
                            
        bfs()
            
        return mat
        
