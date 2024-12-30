class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True