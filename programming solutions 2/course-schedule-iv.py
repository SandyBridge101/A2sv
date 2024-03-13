class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        space=[[float('inf') for i in range(numCourses)] for _ in range(numCourses)]

        for u,v in prerequisites:
            space[u][v]=1

        for i in range(numCourses):
            space[i][i]=0

        for k in range(numCourses):
            for u in range(numCourses):
                for v in range(numCourses):
                    space[u][v]=min(space[u][v],space[u][k]+space[k][v])
        
        print(space)
        res=[]

        for a,b in queries:
            if space[a][b]!=0 and space[a][b]!=float('inf'):
                res.append(True)
            else:
                res.append(False)
        
        return res