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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        e=len(edges)

        for x,y in edges:
            dsu=UnionFind(e+1)
            for u,v in edges:
                
                if u!=x or v!=y:
                    dsu.union(u,v)
            root=dsu.find(1)
            is_edge=False
            for i in range(1,e+1):
                d=dsu.find(i)
                if root!=d:
                    is_edge=True
                    break
            if is_edge==False:
                ans=[x,y]
        return ans

            


        
