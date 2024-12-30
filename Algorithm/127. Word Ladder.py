class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            curr_word, count = q.popleft()
            if curr_word == endWord:
                return count
            for i in range(L):
                int_word = curr_word[:i] + '*' + curr_word[i + 1:]
                for word in all_combo_dict[int_word]: 
                    if word not in seen:
                        seen.add(word)
                        q.append((word, count + 1))
        return 0