class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        n=0

        for e1,e2 in edges:
            n=max(n,e1)
            n=max(n,e2)
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        for key in adj:
            if len(adj[key])==n-1:
                return key
        return 0
