arr=[1,2,3,4,5,6,7,8,9]
arr2=[1,2,3,4,6,5,7,8,9]
#arr=arr[2:6:-1]
arr[2:6]=reversed(arr[2:6])

print(arr)