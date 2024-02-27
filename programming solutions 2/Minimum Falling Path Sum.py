class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])

        for i in range(1,n):
            for j in range(m):
                l,t,r=100000,100000,100000
                s=0
                if 0<=i-1<n and 0<=j<m:
                    t=matrix[i-1][j]
                if 0<=i-1<n and 0<=j+1<m:
                    r=matrix[i-1][j+1]
                if 0<=i-1<n and 0<=j-1<m:
                    l=matrix[i-1][j-1]
                matrix[i][j]+=min([t,l,r])

        print(matrix)
                
        return min(matrix[n-1])
