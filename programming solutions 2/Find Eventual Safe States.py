class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ind=defaultdict(int)
        terminal=deque()
        res=[]
        rev_graph=defaultdict(list)
        queue=deque()
        n=len(graph)

        for i in range(n):
            ind[i]=0

        for i in range(n):
            for c in graph[i]:
                rev_graph[c].append(i)
                ind[i]+=1
        
        for n in ind:
            if ind[n]==0:
                queue.append(n)
        
        #print(queue)
        while queue:
            #print(queue)
            curr=queue.popleft()
            res.append(curr)
            for g in rev_graph[curr]:
                ind[g]-=1
                if ind[g]==0:
                    queue.append(g)
        #print(rev_graph,ind,res) 
        return sorted(res)       
