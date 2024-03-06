class UnionFind:
    def __init__(self,n,m):
        self.root=defaultdict(tuple)
        self.size=[[1 for _ in range(m)] for l in range(n)]
        #print(self.size)
        for i in range(n):
            for j in range(m):
                self.root[(i,j)]=(i,j)
        

    def find(self,x):
        if x==self.root[x]:
            return x
        self.root[x]=self.find(self.root[x])
        return self.root[x]


    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)

        if rootX>rootY:
            self.root[rootY]=rootX
            self.size[rootX[0]][rootX[1]]+=self.size[rootY[0]][rootY[1]]
        else:
            self.root[rootX]=rootY
            self.size[rootY[0]][rootY[1]]+=self.size[rootX[0]][rootX[1]]


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dir={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }
        compatibles={
            1:[{1,4,6},{1,3,5}],
            2:[{2,3,4},{2,5,6}],
            3:[{1,4,6},{5,6,2}],
            4:[{1,3,5},{5,6,2}],
            5:[{1,4,6},{2,3,4}],
            6:[{1,3,5},{2,4,4}]
        }
        n,m=len(grid),len(grid[0])
        rb,cb=n-1,m-1
        dsu=UnionFind(n,m)

        for i in range(n):
            for j in range(m):
                p=0
                for u,v in dir[grid[i][j]]:
                    x,y=u+i,v+j
                    if 0<=x<n and 0<=y<m:
                        if grid[x][y] in compatibles[grid[i][j]][p]:
                            dsu.union((i,j),(x,y))
                    p+=1

        #print(dsu.root)
        #print(rb,cb)
        return True if dsu.find((0,0))==dsu.find((rb,cb)) else False
