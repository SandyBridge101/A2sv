class NumArray:

    def __init__(self, nums: List[int]):
        self.ps=[]
        self.ps.append(nums[0])
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            self.ps.append(nums[i])



    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.ps[right]
        
        return self.ps[right]-self.ps[left-1]


        
