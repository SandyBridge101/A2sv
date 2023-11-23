
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       if len(stones)==1:
           return stones[0]
       nums=[-1*i for i in stones]
       heapq.heapify(nums)
       while len(nums)>1:
           y=heapq.heappop(nums)
           x=heapq.heappop(nums)
           heapq.heappush(nums,y-x)
           print(y,x,y-x)

       print(nums)
       return nums[0]*-1
