class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        top = 0
        bottom = length - 1
        while top < bottom:
            temp = matrix[top]
            matrix[top] = matrix[bottom]
            matrix[bottom] = temp
            top += 1
            bottom -= 1
        for i in range(length):
            for j in range(i+1,length):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp