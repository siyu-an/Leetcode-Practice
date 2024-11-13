class Solution:
    def isHappy(self, n: int) -> bool:
        happy = set()
        def add_all_digits(n):
            output = 0
            while n:
                temp = n % 10
                output += temp ** 2
                n = n // 10
            return output
        while n not in happy:
            happy.add(n)
            n = add_all_digits(n)
            if n == 1:
                return True
        return False
                