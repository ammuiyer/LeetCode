class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = len(s)
        for i in range (len(s)-1):
            if s[start-1]!=" ": break
            else:
                start = start-1
        print(start)
        for i in range (start):
            if s[start-1-i]==" ": break
            else:
                count=count+1
        return count
