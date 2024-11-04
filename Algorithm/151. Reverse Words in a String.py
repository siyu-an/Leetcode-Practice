class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split(' ')
        strings = strings[::-1]
        strings = [word for word in strings if word]
        reverse = ' '.join(strings)
        return reverse