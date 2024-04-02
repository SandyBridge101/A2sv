class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        ans=0
        heights.append(0)

        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                index=stack.pop()
                x=(i-stack[-1]-1)*heights[index]
                ans=max(ans,x)
            stack.append(i)
        return ans
