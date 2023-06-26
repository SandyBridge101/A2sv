dimensions=list(map(int,input().split()))

mat_row=dimensions[0]
mat_col=dimensions[1]
matrix=[]
output_word=[]
for x in range(0,mat_row):
    matrix.append(list(input()))
    
#print(matrix)

for r in range(0,len(matrix)):
    for c in range(0,len(matrix[0])):
        
        row=matrix[r]
        col=[matrix[x][c] for x in range(0,mat_row)]
        #row.remove(matrix[r][c])
        #col.remove(matrix[r][c])
        #print(matrix[r][c],row.count(matrix[r][c]),col.count(matrix[r][c]))
        
        if row.count(matrix[r][c])==1 and col.count(matrix[r][c])==1:
            
            #print(matrix[r][c])
            output_word.append(matrix[r][c])
            
print(''.join(output_word))