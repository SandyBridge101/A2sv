def selectionSort(self, arr,n):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
            
arr=[3,2,7,1,9,5]

print(selectionSort(arr,0))