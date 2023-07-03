names = ["Mary","John","Emma"]
heights = [180,165,170]

arr=list(tuple(zip(names,heights)))
#arr.sort(key=lambda x:x[1],reverse=True)

for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j][1]<arr[j+1][1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print([i[0] for i in arr])