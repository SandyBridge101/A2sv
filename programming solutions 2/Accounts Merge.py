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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mails=defaultdict(int)
        user=defaultdict(set)
        res=defaultdict(set)
        ans=[]
        dsu=UnionFind(len(accounts))

        for i in range(len(accounts)):
            for email in accounts[i][1:len(accounts[i])]:
                user[i].add(email)

                if email not in mails:
                    mails[email]=i
                else:
                    #print(i,mails[email])
                    dsu.union(i,mails[email])
                    mails[email]=i

        
        for i in range(len(accounts)):
            p=dsu.find(i)
            #print(i,p)
            res[p]=res[p].union(user[i])
        #print(res)
        for r in res:
            a=[accounts[r][0]]+sorted(list(res[r]))
            ans.append(a)

        #print(mails['David3@m.co'])
        return ans



