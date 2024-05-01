class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = -1
        if ch in word:
            ind = word.index(ch)
        return word[:ind+1][::-1] + word[ind+1:]