class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums[:k]
        heapq.heapify(self.nums)
        for i in range(k,len(nums)):
            if nums[i]>self.nums[0]:
                heapq.heappushpop(self.nums,nums[i])

        
        

    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        elif self.nums[0]<val:
            heapq.heappushpop(self.nums,val)
        
        return self.nums[0]
