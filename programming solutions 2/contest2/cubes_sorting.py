def bubble_sort(arr,operations):
    n = len(arr)
    swap=0
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap+=1
        if swap>operations:return "NO"
        
    return "YES"
                
N=int(input())

for _ in range(N):
    n=int(input())
    arr=list(map(int,input().split()))
    operations=int(((n*(n-1))/2)-1)
    swaps=0
    decreasing=False
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            decreasing=True
        else:
            decreasing=False
            break
    
    if decreasing==False:print("YES")
    else:print("NO")