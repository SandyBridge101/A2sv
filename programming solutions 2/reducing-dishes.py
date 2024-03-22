class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        index=res=curr=0
        satisfaction.sort()

        for i in range(len(satisfaction)-1,-1,-1):
            curr=satisfaction[i]
            #print(curr,index)

            if index+curr<0:return res

            index+=curr
            res+=index

        return res