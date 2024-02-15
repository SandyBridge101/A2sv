class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n=len(nums)
        min_diff=10**10
        nums.sort()
        if n<=4:
            return 0

        for i in range(0,4):
            for j in range(n-4,n):
                print(nums[i],nums[j],abs(nums[i]-nums[j]))
                if i!=j and (i-0)+((n-1)-j)<=3:
                    min_diff=min(min_diff,abs(nums[i]-nums[j]))
        return min_diff
