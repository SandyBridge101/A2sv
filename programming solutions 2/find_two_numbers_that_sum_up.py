arr=[2,3,4,5,6,7,9]

p1=0
p2=len(arr)-1
target=6
while p1!=p2:
    sum=arr[p1]+arr[p2]
    
    if sum==target:print(arr[p1],arr[p2])
    
    if sum>target:
        p2-=1
    else:
        p1+=1