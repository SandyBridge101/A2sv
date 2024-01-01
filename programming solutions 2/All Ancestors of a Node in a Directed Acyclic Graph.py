class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph=defaultdict(list)
        ind=defaultdict(int)
        res=defaultdict(set)
        queue=deque()

        for i in range(n):
            res[i]=set()
            graph[i]=[]
            ind[i]=0
        for f,t in edges:
            graph[f].append(t)
            ind[t]+=1
        for i in range(n):
            if ind[i]==0:
                queue.append((i,[]))

        while queue:
            #print(queue)
            curr,par=queue.popleft()

            for g in graph[curr]:
                res[g].add(curr)
                res[g].update(res[curr])
                ind[g]-=1
                if ind[g]==0:
                    queue.append((g,[curr]+par))

        ans=[]
        for r in res:
            ans.append(sorted(list(res[r])))
        #print(res)
        return ans
