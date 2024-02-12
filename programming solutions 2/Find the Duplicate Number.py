class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=max(nums)
        index=[i for i in range(n)]
        d=defaultdict(int)

        for k in nums:
            d[k-1]+=1
            if d[k-1]>1:
                return k

        return -1
