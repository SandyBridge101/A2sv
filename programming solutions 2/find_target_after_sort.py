def sort(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

nums = [1,2,5,2,3]
target = 2
indicies=[]
sort(nums)

#print(nums)

for i in range(0,len(nums)):
    if nums[i]==target:
        indicies.append(i)

print(indicies)