class Solution:
    def trailingZeroes(self, n: int) -> int:
        five_power = 5
        count = 0
        while five_power <= n:
            count += n // five_power
            five_power *= 5
        return count
