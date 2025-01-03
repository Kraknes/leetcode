
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zerotupel = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    a = (i,j)
                    zerotupel.append(a)
                 
        for x in range(len(zerotupel)):
            b = zerotupel[x]
            for y in range(len(matrix)):
                matrix[y][b[1]] = 0
            for z in range(len(matrix[i])):
                matrix[b[0]][z] = 0

        