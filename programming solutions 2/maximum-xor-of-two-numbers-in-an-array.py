

class Solution:
    def __init__(self):
        self.root={}

    def findMaximumXOR(self, nums: List[int]) -> int:
        ln=len(bin(max(nums))) - 2 

        for num in nums:
            curr=self.root
            for k in range(31,-1,-1):
                val=1 if num&(1<<k) else 0
                if val not in curr:
                    curr[val]={}   
                curr=curr[val]
            curr['v']=num
        ans=0

        for num in nums:
            curr=self.root
            for k in range(31,-1,-1):
                val=1 if num&(1<<k) else 0
                curr=curr[1-val] if 1-val in curr else curr[val]
            ans=max(ans,num^curr['v'])
    
        return ans
        