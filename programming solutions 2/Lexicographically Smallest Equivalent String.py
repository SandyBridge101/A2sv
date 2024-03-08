class UnionFind:
    def __init__(self,n):
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alphabet=[chr(i) for i in range(97,123)]
        n=len(s1)
        res=''
        dsu=UnionFind(n)
        for i in range(n):
            dsu.union(s1[i],s2[i])

        for b in baseStr:
            for a in alphabet:
                if dsu.find(b)==dsu.find(a):
                    res+=a
                    break
        return res


#indices must be numbers not letters


