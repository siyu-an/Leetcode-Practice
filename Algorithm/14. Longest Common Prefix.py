#leetcode algorithem
#14. Longest Common Prefix(easy)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if strs in empty, return ''
        if not strs: return ''
        # sort strs by alphabetical order and length, s1 is the first string and s2 is the last
        s1=min(strs)
        s2=max(strs)
        # use enumerate() to separate every letter in s1 to see if it appears in s2 at the same location
        for i, c in enumerate(s1):
            #if not match, return all previous letters
            if s2[i]!=c:
                return s1[:i]
        #if no return from for loop, that means s1 is the common prefix
        return s1
