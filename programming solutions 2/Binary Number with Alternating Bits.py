class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev=-1

        while n>0:
            b=n%2
            if prev==-1:
                prev=b
            elif prev==b:
                return False
            prev=b
            n=n//2
        return True
        
