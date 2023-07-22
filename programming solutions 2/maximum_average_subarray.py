nums = [1,12,-5,-6,50,3]
k = 4

l=0
r=0
curr=maxav=0
for r in range(0,len(nums)):
    curr+=nums[r]
    if r<k-1:
        continue
    if r==(k-1):
        maxav=(curr/k)
        continue
    if r>=(k-1):
        curr-=nums[l]
        l+=1
        maxav=max((curr/k),maxav)
        
print(maxav)