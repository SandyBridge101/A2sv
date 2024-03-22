class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)

        p_sum=0
        count={0:1}
        dct={}
        c=0
        k=sum(nums)%p
        mn=n

        if k==0:return 0

        for i in range(len(nums)):
            p_sum+=nums[i]
            if (p_sum-k)%p==0:
                mn=min(mn,i+1)
            if (p_sum-k)%p in dct:
                mn=min(mn,i-dct[(p_sum-k)%p])
            dct[p_sum%p]=i

        return mn if mn!=n else -1


        print(p_sum,c)

        return 0

        
        