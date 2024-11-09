class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zero_col = []
        zero_row = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.append(i)
                    zero_col.append(j)
        for j in zero_col:
            for i in range(row):
                matrix[i][j] = 0
        for i in zero_row:
            matrix[i] = [0]*col