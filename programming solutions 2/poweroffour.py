class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def pow4(n):
            if n==1 :
                return True
            if n<1:
                return False
            else:
                return pow4(n/3)
            
        return pow4(n)
        
