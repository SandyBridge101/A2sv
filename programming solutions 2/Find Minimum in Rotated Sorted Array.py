class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low,high=0,n-1

        if n==1:
            return nums[0]

        if nums[low]<nums[high]:
            return nums[0]

        while low<high:
            mid=low+(high-low)//2

            if nums[mid]>nums[low]:
                low=mid
            else:
                high=mid
        return nums[high+1]
