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
    ch=""
    for i in range(0,len(arr)):
        swaps+=len([arr[k] for k in range(i+1,n) if arr[k]<arr[i]])
        if swaps>operations: break
    #print(swaps,operations)
    if swaps<=operations:
        print("YES")
    else:
        print("NO")