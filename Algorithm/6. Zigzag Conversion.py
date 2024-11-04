class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        turn = 0
        res = [''] * numRows
        while i < len(s):
            if turn == 0:
                row = i % (numRows - 1)
                res[row] += s[i]
            else:
                row = (numRows - 1) - (i % (numRows - 1))
                res[row] += s[i]
            i += 1
            if i % (numRows - 1) == 0:
                turn = (turn + 1) % 2
        return ''.join(res) 
