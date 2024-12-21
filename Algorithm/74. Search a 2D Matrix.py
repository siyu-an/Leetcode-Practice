class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid + 1
        row = (top + bot) // 2
        lt_pt = 0
        rt_pt = len(matrix[row]) - 1
        while lt_pt <= rt_pt:
            mid_pt = (lt_pt + rt_pt)//2
            if target == matrix[mid][mid_pt]:
                return True
            elif target < matrix[mid][mid_pt]:
                rt_pt = mid_pt - 1
            else:
                lt_pt = mid_pt + 1
        return False