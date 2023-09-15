class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        #print(bisect_left(nums,target),bisect_right(nums,target))
        return bisect_left(nums,target)
        #that's sooo criminal....
