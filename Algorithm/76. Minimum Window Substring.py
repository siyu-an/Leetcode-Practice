class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, seen, target, res = 0, Counter(), Counter(t), [inf, '']
        for end in range(len(s)):
            seen[s[end]] += 1
            while seen >= target:
                res = min(res, [end-start+1, s[start:end+1]])
                seen[s[start]] -= 1
                start += 1
        
        return res[1]