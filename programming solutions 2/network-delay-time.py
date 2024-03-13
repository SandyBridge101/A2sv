class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        space=[[float('inf') for i in range(1,n+1)] for _ in range(1,n+1)]

        for u,v,w in times:
            space[u-1][v-1]=w

        for i in range(n):
            space[i][i]=0
        
        for j in range(n):
            for u in range(n):
                for v in range(n):
                    space[u][v]=min(space[u][v],space[u][j]+space[j][v])
        
        print(space)
        res=-1
        x=0
        if float('inf') in space[k-1]:
            return res
        
        for m in space[k-1]:
            #print(m)
            if  m!=0 and m!=float('inf'):
                res=max(m,res)
            x+=1
        return res

