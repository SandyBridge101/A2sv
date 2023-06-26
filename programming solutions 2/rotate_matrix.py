matrix = [[1,2,3],[4,5,6],[7,8,9]]

ref=tuple(matrix)

print(matrix,ref)
r = len(ref)-1
for c in range(0,len(ref[0])):
    print(matrix[r][c])
    row=[ref[i][c] for i in range(len(ref)-1,-1,-1)]
    matrix[c]=row
    print(row)
    
print(matrix)