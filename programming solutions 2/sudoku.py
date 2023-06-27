board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def check_sudoku(board):
    dimension=9
    for r in range(0,len(board)):
        row=[int(board[r][i]) for i in range(0,len(board[r])) if board[r][i]!='.']
        for i in row:
            if i>9:
                print("invalid, out of range")
                return False
        if len(row)==len(set(row)):print(row,"valid")
        else:
            print("invalid,row")
            return False
    #for c in range(1,len(board[0])):
    print("col")
    for c in range(0,len(board[0])):
        col=[int(board[i][c]) for i in range(0,len(board[r])) if board[i][c]!='.']
        for i in col:
            if i>9:
                print("invalid, out of range")
                return False
        print(col)
        if len(col)==len(set(col)):print(col,"valid")
        else:
            print("invalid,col")
            return False

    for r in range(1,len(board),3):
        for c in range(1,len(board[0]),3):
            #print(board[r][c])
            mat=[]
            cell=board[r][c]
            left=board[r][c+1]
            right=board[r][c-1]
            top=board[r-1][c]
            down=board[r+1][c]
            u_left=board[r-1][c+1]
            u_right=board[r-1][c-1]
            d_left=board[r+1][c+1]
            d_right=board[r+1][c-1]
            if cell!='.':mat.append(cell)
            if left!='.':mat.append(left)
            if right!='.':mat.append(right)
            if top!='.':mat.append(top)
            if down!='.':mat.append(down)
            if u_left!='.':mat.append(u_left)
            if u_right!='.':mat.append(u_right)
            if d_left!='.':mat.append(d_left)
            if d_right!='.':mat.append(d_right)
            #mat=[cell,left,right,top,down,u_left,u_right,d_left,d_right]
            
            if len(mat)==len(set(mat)):
                print(cell,"valid")
            else:
                print("invalid,cell")
                return False
            

    return True


print(check_sudoku(board))