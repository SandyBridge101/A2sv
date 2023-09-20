class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow3(n):
            if n==1 :
                return True
            if n<1:
                return False
            else:
                return pow3(n/3)
            
        return pow3(n)
