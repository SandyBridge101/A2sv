class UnionFind:
    def __init__(self):
        self.root={chr(i):chr(i) for i in range(97,123)}
        self.size={chr(i):0 for i in range(97,123)}

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
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu=UnionFind()

        for eqn in equations:
            if eqn[1]=='=':
                dsu.union(eqn[0],eqn[3])

        for eqn in equations:
            if eqn[1]=='!':
                if dsu.find(eqn[0])==dsu.find(eqn[3]):
                    return False

        return True


        
