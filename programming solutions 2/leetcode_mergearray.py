nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

p1=len(nums1)-1
p2=len(nums2)-1

for p2 in range(len(nums2)-1,-1,-1):
    nums1[p1]=nums2[p2]
    p1-=1
nums1.sort()
print(nums1)