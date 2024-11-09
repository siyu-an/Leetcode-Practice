class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_sort = ''.join(sorted(ransomNote))
        m_sort = ''.join(sorted(magazine))
        for r in r_sort:
            if r in m_sort:
                idx = m_sort.find(r)
                m_sort = m_sort[idx+1:]
            else:
                return False
        return True