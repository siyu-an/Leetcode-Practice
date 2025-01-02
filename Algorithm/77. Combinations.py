class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first_num):
            if len(curr) == k:
                output.append(curr[:])
                return
            need = k - len(curr)
            remain = n - first_num + 1
            available = remain - need
            for num in range(first_num, first_num + available + 1):
                curr.append(num)
                backtrack(num + 1)
                curr.pop()
        curr = []
        output = []
        backtrack(1)
        return output
