#grid = [[4,7,8],[9,5,1],[2,3,6]]
#grid=[[4,3,8,4],[9,5,1,9],[2,7,6,2]]
grid=[[10,3,5],[1,6,11],[7,9,2]]
count=0

if len(grid)==3 and len(grid[0])==3:
    print(count)

for r in range(1,len(grid)-1):
    if len(set(grid[r]))==1:
        count=0
        break
    for c in range(1,len(grid[0])-1):
        #print(grid[r][c])
        #row
        row_sum=grid[r][c]+grid[r][c+1]+grid[r][c-1]
        col_sum=grid[r][c]+grid[r+1][c]+grid[r-1][c]
        left_d=grid[r][c]+grid[r-1][c-1]+grid[r+1][c+1]
        right_d=grid[r][c]+grid[r-1][c+1]+grid[r+1][c-1]
        top_row=grid[r-1][c]+grid[r-1][c+1]+grid[r-1][c-1]
        down_row=grid[r+1][c]+grid[r+1][c+1]+grid[r+1][c-1]
        left_col=grid[r][c-1]+grid[r+1][c-1]+grid[r-1][c-1]
        right_col=grid[r][c+1]+grid[r+1][c+1]+grid[r-1][c+1]
        
        print(row_sum,col_sum,left_d,right_d,top_row,down_row,left_col,right_col)
        if row_sum==col_sum and row_sum==left_d and row_sum==right_d and row_sum==top_row and row_sum==down_row and row_sum==left_col and row_sum==right_col:
            if grid[r][c]<10 and grid[r-1][c]<10 and grid[r-1][c-1]<10 and grid[r-1][c+1]<10 and grid[r][c-1]<10 and grid[r][c+1]<10 and grid[r+1][c]<10 and grid[r+1][c+1]<10 and grid[r+1][c-1]<10:
                count+=1

print(count)