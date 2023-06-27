#arr=[2,3,4,5,2,1,0]
arr=[0,1,2,1,2]
peak=0
low=0
if len(arr)==2:
    print(False)
    
for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        peak+=1
    if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
        low+=1
print(peak)

if peak==1 and low==0:
    print(True)
elif low>=1:
    print(False)
else:
    print(False)