class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vs=set()
        graph=defaultdict(list)
        for i in range(len(isConnected)):
            graph[i]=[j for j in range(len(isConnected[0])) if isConnected[i][j]==1]
        def dfs(node):
            if (node in vs):
                return
            vs.add(node)
            for n in graph[node]:
                dfs(n)
        dfs_calls=0
        for node in list(graph):
            if node not in vs:
                dfs_calls+=1
                dfs(node)
        return dfs_calls
