#67. Add Binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a),len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry_over = 0
        output = []
        for i in range(n-1,-1,-1):
            if int(a[i]) + int(b[i]) + carry_over <= 1:
                output.append(str(int(a[i]) + int(b[i])+carry_over))
                carry_over = 0
            elif int(a[i]) + int(b[i]) + carry_over == 2:
                output.append('0')
                carry_over = 1
            else:
                output.append('1')
                carry_over = 1
        if carry_over == 1:
            output.append('1')
        output.reverse()
        return ''.join(output)
                