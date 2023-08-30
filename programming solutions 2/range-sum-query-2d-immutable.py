class NumMatrix:
    pm=[]
    def __init__(self, matrix: List[List[int]]):
        self.pm=[[0]*len(matrix[0]) for i in range(0,len(matrix))]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                #self.pm[i][j]=(matrix[i][j]+p[i-1][j]+p[i][j-1])-p[i-1][j-1]
                if (i==0) and (j==0):
                    self.pm[0][0]=matrix[0][0]
                elif i==0 and j>0:
                    self.pm[i][j]=matrix[i][j]+self.pm[i][j-1]
                elif j==0 and i>0:
                    self.pm[i][j]=matrix[i][j]+self.pm[i-1][j]
                else:
                    self.pm[i][j]=(matrix[i][j]+self.pm[i-1][j]+self.pm[i][j-1])-self.pm[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=self.pm[row2][col2]

        if row1>0 and col1>0:
            sum+=self.pm[row1-1][col1-1]
        if col1>0:
            sum-=self.pm[row2][col1-1]
        if row1>0:
            sum-=self.pm[row1-1][col2]

        return sum
