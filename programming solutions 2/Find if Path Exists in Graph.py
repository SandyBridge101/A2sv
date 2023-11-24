class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=defaultdict(list)
        visited=set()
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        print(adj)

        def path(source):
            if source==destination:
                #print('f')
                return True
            visited.add(source)
            for node in adj[source]:
                if node not in visited:
                    if path(node): return True

        return path(source)
