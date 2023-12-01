
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

#test case: [[1,10,[2,3,4]],[2,-1,[]],[3,-2,[]],[4,-3,[]]] id: 2
#consider level
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        data=defaultdict(Employee)
        imp=[]
        vs=set()
        for emp in employees:
            graph[emp.id]=emp.subordinates
            data[emp.id]=emp

        def dfs(node,is_sub):
            if not node or (node in vs):
                return
            if id==node.id:
                is_sub=1
            if is_sub==1:
                vs.add(node)
                imp.append(node.importance)
            for sub in node.subordinates:
                dfs(data[sub],is_sub)

        for emp in employees:
            
            dfs(emp,0)
        
        return sum(imp)
