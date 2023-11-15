
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        #print(len(nums))

        while True:
            if len(nums)==k:
                break
            heapq.heappop(nums)

        return heapq.heappop(nums)
        
