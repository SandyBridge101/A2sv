class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=-1
        p1=0
        p2=n-1

        while p1<p2:
            max_area=max(max_area,(p2-p1)*min(height[p2],height[p1]))

            if height[p1]<height[p2]:
                p1+=1
            elif height[p2]<height[p1]:
                p2-=1
            else:
                p1+=1
                p2-=1
        
        return max_area
