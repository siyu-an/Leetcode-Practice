def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl = len(words[0])
        k = len(words)
        substring_len = k * wl
        if len(s) < substring_len:
            return []
        dic = collections.Counter(words)
        def check(i):
            temp = dic.copy()
            word_used = 0
            for j in range(i,i + substring_len, wl):
                word_check = s[j:j+wl]
                if temp[word_check] > 0:
                    temp[word_check] -= 1
                    word_used += 1
                else:
                    break
            return word_used == k
        ans = []
        for i in range(len(s) - substring_len + 1):
            if check(i):
                ans.append(i)
        return ans
