class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=defaultdict(list)
        color={}
        vs=set()

        for d in dislikes:
            graph[d[0]].append(d[1])
            graph[d[1]].append(d[0])
        
        #re-implement
        def dfs(node,p):
            color[node]=p
            for g in graph[node]:
                if g in color:
                    if color[g]==p:
                        return False
                else:
                    if not dfs(g,1-p):
                        return False

            return True

            

        for node in range(1,n+1):
            if node not in color:
                if not dfs(node,1):
                    print(color)
                    return False
                print(color)
        
        return True
