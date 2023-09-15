class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        res=-1

        while low<=high:
            mid=low+(high-low)//2
            #print(mid)
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]==target:
                return mid

        return res

        
