#mat=[[1,2],[3,4]]
#mat=[[1,2,3],[4,5,6],[7,8,9]]
#mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#mat=[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

mat=[[2,5],[8,4],[0,-1]]

new=[]
def matrix_spiral(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return
    if len(matrix)==1:
        new.extend(matrix[0])
        print(new)
        return
    
    if len(matrix[0])==1:
        for i in matrix:
            new.extend(i)
        print(new)
        return
    
    if len(matrix)==2:
        new.extend(matrix[0])
        matrix.pop(0)


        col=len(matrix[0])-1

        for row in range(0,len(matrix)):
            new.append(matrix[row][col])
            matrix[row].pop(col)

        new.extend([matrix[len(matrix)-1][i] for i in range(len(matrix[len(matrix)-1])-1,-1,-1)])
        matrix.pop(len(matrix)-1)
        return
    


    new.extend(matrix[0])
    matrix.pop(0)

    print(matrix)

    col=len(matrix[0])-1

    for row in range(0,len(matrix)):
        new.append(matrix[row][col])
        matrix[row].pop(col)

    print(matrix)


    new.extend([matrix[len(matrix)-1][i] for i in range(len(matrix[len(matrix)-1])-1,-1,-1)])
    #new.extend(sorted(matrix[len(matrix)-1],reverse=True))
    matrix.pop(len(matrix)-1)

    print(matrix)

    col=0

    for row in range(len(matrix)-1,-1,-1):
        new.append(matrix[row][col])
        matrix[row].pop(col)

    print(matrix)

    print(new)
    
    matrix_spiral(matrix)
    
matrix_spiral(mat)
print(new)