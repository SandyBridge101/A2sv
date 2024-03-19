class Solution:
    def countPrimes(self, n: int) -> int:
        primes=set()
        state=[False]*(n+1)

        for i in range(2,n):
            if state[i]==False:
                j=2
                while i*j<n:
                    state[i*j]=True
                    j+=1

        return len(set([i for i in range(2,n) if state[i]==False]))
        