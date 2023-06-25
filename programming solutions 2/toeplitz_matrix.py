matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

for r in range(0,len(matrix)):
    c=0
    row,col=r,c
    diagonal=[]
    print(matrix[row][col],(row,col))
    diagonal.append(matrix[row][col])
    while row<len(matrix)-1 and col<len(matrix[0])-1:
        row+=1
        col+=1
        print(matrix[row][col],(row,col))
        diagonal.append(matrix[row][col])
    print(diagonal)
    if len(set(diagonal))!=1:print(False)

for c in range(1,len(matrix[0])):
    r=0
    row,col=r,c
    diagonal=[]
    print(matrix[row][col],(row,col))
    diagonal.append(matrix[row][col])
    while row<len(matrix)-1 and col<len(matrix[0])-1:
        row+=1
        col+=1
        print(matrix[row][col],(row,col))
        diagonal.append(matrix[row][col])
    print(diagonal)
    if len(set(diagonal))!=1:print(False)


