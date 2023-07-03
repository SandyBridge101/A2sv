mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
k = 1

def get_block(r,c,k,arr):
    start_row=r-k-1
    start_col=c-k-1
    #if start_row<0:start_row=0
    #if start_col<0:start_col=0
    sum=0
    print(start_row,start_col)
    for row in range(start_row,(2*k)+2):
        for col in range(start_col,(2*k)+2):
            #print(arr[row][col])
            if 0<=row<len(arr) and 0<=col<len(arr[0]):
                print(row,col,arr[row][col])
                sum+=arr[row][col]
    return sum


print(get_block(0,0,1,mat))

