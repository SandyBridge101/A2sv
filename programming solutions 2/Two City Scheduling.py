class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)

        d=[]
        for i in range(n):
            d.append([costs[i][0]-costs[i][1],i])
        d.sort()

        s=0
        for i in range(n):
            if i<n//2:
                s+=costs[d[i][1]][0]
            else:
                s+=costs[d[i][1]][1]
    

        return s
