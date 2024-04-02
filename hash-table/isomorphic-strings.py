class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tcopy = ""
        dict = {}
        values = set()
        for i in range(0, len(s)):
            if s[i] in dict:
                if t[i]!=dict[s[i]]:
                    return False
            else:
                dict[s[i]] = t[i]
                currlen = len(values)
                values.add(t[i])
                if currlen == len(values):
                    return False
        
        return True

        
        