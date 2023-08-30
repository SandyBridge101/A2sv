class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        
        for i in range(0,len(nums)):
            if nums[i]-k in freq:
                count+=freq[nums[i]-k]
            
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        return count
