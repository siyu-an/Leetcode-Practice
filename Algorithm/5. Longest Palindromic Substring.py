class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                curr = s[i : j + 1]
                if curr == curr[::-1] and len(curr) > len(ans):
                    ans = curr
        return ans