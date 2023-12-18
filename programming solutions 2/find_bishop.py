t=int(input())

def solve():
    chess=[]
    for _ in range(8):
        chess.append(input())
    for i in range(1,len(chess)-1):
        for j in range(1,len(chess[0])-1):
            #print(i,j)
            if chess[i][j]=='#' and chess[i+1][j+1]=='#' and chess[i-1][j-1]=='#' and chess[i+1][j-1]=='#' and chess[i-1][j+1]=='#':
                print(i+1,j+1)

for _ in range(t):
    input()
    solve()
