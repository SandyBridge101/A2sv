class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph=defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        min_dist={i:[float('inf'),0] for i in graph.keys()}
        min_dist[0]=[0,1]

        heap=[(0,0)]
        
        while heap:
            cost,node=heapq.heappop(heap)

            if cost>min_dist[n-1][0]:
                break

            for child in graph[node]:
                if (cost+child[1])>min_dist[child[0]][0]:
                    continue
                elif cost+child[1]==min_dist[child[0]][0]:
                    min_dist[child[0]][1]+=min_dist[node][1]
                else:
                    min_dist[child[0]][0]=cost+child[1]
                    min_dist[child[0]][1]=min_dist[node][1]
                    heapq.heappush(heap,(cost+child[1],child[0]))                


        return min_dist[n-1][1]%(pow(10,9)+7)
