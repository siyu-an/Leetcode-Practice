class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_hash = {}
        s_hash = {}
        s = s.split(' ')
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in p_hash:
                p_hash[pattern[i]] = i
            if s[i] not in s_hash:
                s_hash[s[i]] = i
            if s_hash[s[i]] != p_hash[pattern[i]]:
                return False
        return True