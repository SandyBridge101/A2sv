class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls=[0]*(len(nums))
        rs=[0]*(len(nums))
        answer=[]
        ls[0]=0
        for i in range(1,len(nums)):
            ls[i]=ls[i-1]+nums[i-1]
        
        rs[len(nums)-1]=0
        for i in range(len(nums)-2,-1,-1):
            rs[i]=rs[i+1]+nums[i+1]
        
        for i in range(len(nums)):
            answer.append(abs(ls[i]-rs[i]))

        return answer
        
