class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def is_valid_state(state,solutions):
            if len(state)==k:
                return True

        def get_candidates(state):
            candidates=[]
            x=1
            if state:x=state[-1]+1
            for i in range(x,n+1):
                candidates.append(i)
            return candidates

        def search(state,solutions):
        
            if is_valid_state(state,solutions):
                #print("valid ->",state)
                solutions.append(state.copy())
                return
            
            #print(state,"->",get_candidates(state))
            for candidate in get_candidates(state):
                if len(state)<k:
                    state.append(candidate)
                    search(state,solutions)
                    state.remove(candidate)

        
        def solve():
            solutions=[]
            state=[]
            search(state,solutions)
            return solutions
        
        return solve()
