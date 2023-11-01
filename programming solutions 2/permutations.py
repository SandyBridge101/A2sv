class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        def is_valid(state):
            if len(state)==n:
                #print('valid ->',state,n)
                return True
        
        def get_candidates(state):
            candidates=[]
            for num in nums:
                if num not in state:
                    candidates.append(num)
            return candidates
        
        def search(state,solution):
            if is_valid(state):
                solution.append(state.copy())
                return
            #print(state,'->',solution)
            for candidate in get_candidates(state):
                state.append(candidate)
                search(state,solution)
                state.remove(candidate)
        
        def solve():
            solution=[]
            state=[]
            search(state,solution)
            print(solution)
            return solution

        return solve()

        
