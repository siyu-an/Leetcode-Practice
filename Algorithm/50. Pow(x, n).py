class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        res = 1
        curr_pow = x
        n_abs = abs(n)
        while n_abs > 0:
            if n_abs % 2 == 1:
                res *= curr_pow
            curr_pow *= curr_pow
            n_abs //= 2
        if n < 0:
            return 1.0/res
        return res