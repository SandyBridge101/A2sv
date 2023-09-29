class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        r=k-1
        max_sum=0
        sm=sum(nums[0:k-1])
        freq={}
        for i in range(0,k-1):
            freq[nums[i]]=1+freq.get(nums[i],0)
        print(freq)

        for r in range(k-1,n):
            l=r-(k-1)
            sm+=nums[r]
            freq[nums[r]]=1+freq.get(nums[r],0)
            #print(sm,r,freq)
            if len(freq)==k:
                max_sum=max(sm,max_sum)
            sm-=nums[l]
            freq[nums[l]]-=1
            if freq[nums[l]]==0:
                freq.pop(nums[l])

    
        return max_sum

        
