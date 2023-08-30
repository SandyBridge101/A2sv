class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}

        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        
        for i in range(0,len(nums)):
            comp=nums[i]%k

            if comp in freq:
                count+=freq[comp]
                freq[comp]+=1
            else:
                freq[comp]=1
        
        return count
