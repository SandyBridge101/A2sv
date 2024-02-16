class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=[]
        b=[]
        la=0
        lb=0

        while x>0:
            a.append(x%2)
            x=x//2
            la+=1
        
        while y>0:
            b.append(y%2)
            y=y//2
            lb+=1
        i=0
        count=0
        while i<la or i<lb:
            if i<la and i<lb:
                count+=(a[i] ^ b[i])
            elif i<la and i>=lb:
                count+=(a[i] ^ 0)
            elif i>=la and i<lb:
                count+=(0 ^ b[i])
            i+=1
        
        return count
        
