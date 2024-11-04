class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        x = y = 0
        dx = 1
        dy = 0
        for i in range(n**2):
            res[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or res[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x += dx
            y += dy
        return res