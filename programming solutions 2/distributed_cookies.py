class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        state = [0]*k
        ans = sum(cookies)
        
        def search(state, x):
            nonlocal ans
            if x == k:
                if sum(cookies) == 0:
                    ans = min(ans, max(state))
                return
            
            for i in range(len(cookies)):
                if cookies[i] == 0:continue
                state[x] += cookies[i]
                tmp = cookies[i]
                cookies[i] = 0
                if state[x] < ans:
                    search(state, x)
                    search(state, x+1)
                state[x] -= tmp
                cookies[i] = tmp

        search(state, 0)
        return ans
