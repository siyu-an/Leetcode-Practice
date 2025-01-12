class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            for j in range(n):
                if j == n -1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                elif j - 1 >= 0:
                    triangle[i][j] = min(triangle[i][j] + triangle[i-1][j],triangle[i][j] + triangle[i-1][j-1])
                else:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        return min(triangle[-1])
