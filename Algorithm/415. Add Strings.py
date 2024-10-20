# 415. Add Strings
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1>=0 or p2>=0:
            c1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            c2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (c1 + c2 +carry) % 10
            carry = (c1 + c2 +carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])
#Alternative solution
        return str(int(num1)+int(num2)) 
