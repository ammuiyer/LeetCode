class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = {}
        for x in s1.split(" "):
            if x not in s:
                s[x] = 1
            else:
                s[x]+=1
        for x in s2.split(" "):
            if x not in s:
                s[x] = 1
            else:
                s[x]+=1
        ret = []
        for a in s:
            if s[a]==1:
                ret.append(a)
        return ret
        
        