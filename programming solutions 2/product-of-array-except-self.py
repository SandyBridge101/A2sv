class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pp=[]
        ps=[0]*(len(nums))
        answer=[]
        #prefix
        pp.append(1)
        for i in range(1,len(nums)):
            pp.append(pp[i-1]*nums[i-1])
        #print(pp)
        
        ps[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            ps[i]=nums[i+1]*ps[i+1]
        #print(ps)
        
        for i in range(0,len(nums)):
            answer.append(pp[i]*ps[i])
        return answer
      
