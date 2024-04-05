class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while(i<=len(s)-2):
            if (s[i].lower() == s[i+1] and s[i].lower()!=s[i]) or (s[i+1].lower() == s[i] and s[i+1].lower()!=s[i+1]):
                s = s[:i] + s[i+2:]
                print(s)
                if i>0:
                    i=i-1
            else:
                i+=1
        return s