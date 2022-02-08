#28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n]==needle:
                return i
        #if haystack==needle:
            #return 0
        #else:
        return -1