class UnionFind:
    def __init__(self,n):
        self.root=[i for i in range(n)]
        self.size=[1]*n

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
            self.size[rootX]+=self.size[rootY]
        else:
            self.root[rootX]=rootY
            self.size[rootY]+=self.size[rootX]

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        dsu=UnionFind(n)
        number=n
        print(dsu.find(2))
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1 and dsu.find(i)!=dsu.find(j):
                    number-=1
                    dsu.union(i,j)

        return number
        
