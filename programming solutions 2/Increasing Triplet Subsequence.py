class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n=len(nums)
        fst=(2**31)+3
        snd=(2**31)+3
        trd=(2**31)+3

        for i in range(n):
    
            if nums[i]<=fst:
                fst=nums[i]
            elif nums[i]<=snd:
                snd=nums[i]
            else:
                trd=nums[i]
                return True

        return False

