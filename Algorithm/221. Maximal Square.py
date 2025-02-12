from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    if matrix[i][j] == '1':
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                if dp[i][j] > result:
                    result = dp[i][j]
        return result * result
matrix = [['0','0','1'],['1','1','1']]
solution = Solution()
print(solution.maximalSquare(matrix))