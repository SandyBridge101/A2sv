height = [1,8,6,2,5,4,8,3,7]

start=0

end=len(height)-1
max_area=0
while start<=end:
    l=end-start
    h=min(height[end],height[start])
    max_area=max(max_area,l*h)
    
    if height[start]<height[end]:
        start+=1
    elif height[start]>height[end]:
        end-=1
    else:
        start+=1
        
print(max_area)