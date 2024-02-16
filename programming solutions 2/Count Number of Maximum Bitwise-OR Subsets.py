class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n=len(nums)

        opm=0
        ans=[]
        visited=set()
        
        for num in nums:
            opm|=num
        

        def is_valid(state):
            op=0
            for i in state:
                op|=nums[i]
            
            if op==opm:
                #print(op,opm,state)
                return True
            return False
        
        def get_candidates(state):
            candidates=[]
            l=0
            if state:
                l=max(state)+1
            
            for i in range(l,n):
                if i not in state:
                    candidates.append(i)
            return candidates

        def search(state,solution):
            if is_valid(state):
                #print(state,visited)
                solution.append(state.copy())
                
            for candidate in get_candidates(state):
                state.add(candidate)
                search(state,solution)
                state.remove(candidate)

        
        state=set()
        search(state,ans)
        

        return len(ans)
