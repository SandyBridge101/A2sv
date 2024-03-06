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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dsu=UnionFind(n)
        for u,v in edges:
            dsu.union(u,v)
            dsu.union(v,u)

        return True if dsu.find(destination)==dsu.find(source) else False

