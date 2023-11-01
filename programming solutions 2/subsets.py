class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def is_valid(state,solution):
            if len(state)<len(nums):
                return True
            else:
                return False
        
        def get_candidates(state):
            candidates=[]
            x=-11
            if state:x=state[-1]
            for i in nums:
                if i>x:
                    candidates.append(i)
            
            return candidates



        def search(state,solution):
            if not is_valid(state,solution):
                return
            
            #print(state,"->",get_candidates(state))
            solution.append(state.copy())
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state,solution)
                state.remove(candidate)


        def solve():
            state=[]
            solution=[]
            #print(nums)
            search(state,solution)
            solution.append(nums)
            #print(solution)
            return solution
        
        return solve()
