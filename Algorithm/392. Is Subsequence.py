class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if s == t:
            return False
        for i in t:
            if i == s[0] and len(s) > 1:
                s = s[1:]
            elif i==s[0] and len(s) == 1:
                return True
        return False
