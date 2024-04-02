class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*(n)

        for i in range(n):

            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                print(index,i,temperatures[index],temperatures[i])
                res[index]=i-index

            stack.append(i)

        #print(res)

        return res
        