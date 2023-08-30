class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        inter=set(nums1).intersection(set(nums2))
        inter=list(inter)
        inter.sort()

        if len(inter)>0:
            return inter[0]
        else:
            return -1

        
