class Solution:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        else:
            queue = deque()
            queue.append((beginWord, 1))               
            while queue :
                   word, count = queue.popleft()
                   for i in range(len(word)):
                       for j in range(26):
                           new = word[:i] + chr(97+j)+word[i+1:]
                           if new == endWord:
                               return count+1
                           if new in wordList:
                                queue.append((new, count+1))
                                wordList.remove(new)
            return 0
                


                

        