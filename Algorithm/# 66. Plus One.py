# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            index = -1 - i
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits
        return [1] + digits