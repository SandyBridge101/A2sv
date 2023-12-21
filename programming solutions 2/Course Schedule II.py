class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph=defaultdict(list)
        ind=defaultdict(int)
        
        for i in range(numCourses):
            ind[i]=0

        for u,v in prerequisites:
            graph[v].append(u)
            ind[u]+=1
        
        print(ind,graph)
        def bfs():
            res=[]
            queue=deque()
            for n in ind:
                if (ind[n])==0:
                    queue.append(n)
            #print(queue)

            while queue:
                print(queue)
                curr=queue.popleft()
                res.append(curr)

                for g in graph[curr]:
                    ind[g]-=1
                    if ind[g]==0:
                        queue.append(g)
            return res

        ans=bfs()

        if len(ans)==numCourses:
            return ans
        else:
            return []
