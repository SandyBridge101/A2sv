nmat=[]

for r in range(0,len(mat)):

    
    for c in range(0,len(mat[0])):
        center=0
        row_sum=0
        col_sum=0
        diag_sum=0
        print(row_sum,col_sum,diag_sum,mat[r][c])

        
        #top
        row,col=r,c
        while col!=c+k:
            col_sum+=mat[row][col]
            col+=1
        #down
        row,col=r,c
        while col!=c-k:
            col_sum+=mat[row][col]
            col-=1
        #right
        row,col=r,c
        while row!=r+k:
            row_sum+=mat[row][col]
            row+=1
        #left
        row,col=r,c
        while row!=r-k:
            row_sum+=mat[row][col]
            row-=1
        
        #u_left
        row,col=r,c
        while row!=r+k and col!=r+k:
            diag_sum+=mat[row][col]
            row+=1
            col+=1
        #d_right
        row,col=r,c
        while row!=r-k and col!=r-k:
            diag_sum+=mat[row][col]
            row-=1
            col-=1
            
        #u_right
        row,col=r,c
        while row!=r-k and col!=r+k:
            diag_sum+=mat[row][col]
            row-=1
            col+=1
        
        #d_left
        row,col=r,c
        while row!=r+k and col!=r-k:
            diag_sum+=mat[row][col]
            row+=1
            col-=1
            
        sum=row_sum+col_sum+diag_sum+mat[r][c]
        print(row_sum,col_sum,diag_sum,mat[r][c])
        nmat.append(sum)
        
print(nmat)