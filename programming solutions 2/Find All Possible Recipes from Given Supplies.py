class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        out=defaultdict(int)
        graph=defaultdict(list)
        for i in range(len(recipes)):
            out[recipes[i]]=len(ingredients[i])
            for n in ingredients[i]:
                graph[n].append(recipes[i])
        

        print(graph,out)
        
        queue=deque(supplies)
        res=[]

        while queue:
            curr=queue.popleft()
            res.append(curr)

            for g in graph[curr]:
                out[g]-=1
                if out[g]==0:
                    queue.append(g)
    
        ans=[]
        for r in recipes:
            if r in res:
                ans.append(r)
        return ans
        
