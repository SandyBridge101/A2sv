arr = [17,18,5,4,6,1]
mx=-1
arr.reverse()
for i in range(0,len(arr)-1):
    if arr[i]>arr[i+1]:
        arr[i+1]=arr[i]

arr.pop()
arr.reverse()
arr.append(-1)

print(arr)





