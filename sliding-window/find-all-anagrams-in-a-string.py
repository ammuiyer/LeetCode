class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for char in p:
            if char not in d:
                d[char] = 1
            else:
                d[char]+=1
        left = 0 
        right = 0
        ret = []
        while(right<len(s)):
            #check the character ur at
            if s[right] in p: 
                d[s[right]]-=1
                #check if p is emtpy 
                flag = True
                for x, y in zip(d.values(), [0]*len(d.keys())):
                    if x!=y:
                        flag = False
                if flag:
                    #valid
                    ret.append(left)
            right+=1        
            if right-left >= len(p):
                if s[left] in p:
                    d[s[left]]+=1
                left+=1
            

        return ret






        