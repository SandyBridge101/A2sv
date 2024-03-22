class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        mx=-1

        for i in range(n):
            s+=nums[i]
            k=s/(i+1)
            mx=max(k,mx)

        return ceil(mx)