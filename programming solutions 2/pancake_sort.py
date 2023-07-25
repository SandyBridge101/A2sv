arr = [3,2,4,1]


turns=[]
def flip(arr,i):
    turns.append(i)
    return arr[:i+1][::-1] + arr[i+1:]
    
def find_max_index(arr, n):
    max_index=0
    for i in range(n):
        if arr[i]>arr[max_index]:
            max_index=i
    return max_index


for c in range(len(arr),-1,-1):
    mi=find_max_index(arr,c)
    if mi!=c-1:
        arr=flip(arr,mi)
        arr=flip(arr,c-1)
    c-=1

print(turns)