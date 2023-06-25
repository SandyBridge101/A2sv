matrix = [[1,1,1],[1,0,1],[1,1,1]]
tmp=matrix
tmp=[tuple(i) for i in tmp]
print(tmp,matrix)
for r in range(0,len(matrix)):
    for c in range(0,len(matrix[0])):
        #print(matrix[r][c])
        if tmp[r][c]==0:
            row,col=r,c
            #up
            while row!=-1:
                matrix[row][col]=0
                #print(matrix)
                row-=1
            
            row,col=r,c
            #down
            while row!=len(matrix):
                matrix[row][col]=0
                #print(matrix)
                row+=1
            
            row,col=r,c
            #left
            while col!=-1:
                matrix[row][col]=0
                #print(matrix)
                col-=1
            
            #right
            while col!=len(matrix[0]):
                matrix[row][col]=0
                #print(matrix)
                col+=1

print(tmp,matrix)