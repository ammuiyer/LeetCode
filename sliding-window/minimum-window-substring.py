class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0, 0
        d = {}
        for c in t:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        m = s + "_"
        while r < len(s):
            if s[r] in d:
                d[s[r]]-=1
                #check that everthing is 0
                flag = True
                for key in d.keys():
                    if d[key]>0:
                        flag = False
                if flag:
                    #minimize
                    #print(d, l, r)
                    while l<=r:
                        if s[l] in d:
                            d[s[l]]+=1
                            #print(d)
                            if d[s[l]]>0: 
                                newstr = s[l:r+1]
                                if len(newstr)<len(m):
                                    m = newstr
                                break
                        #print(s[l:r+1])
                        l+=1
                    l+=1
            r+=1
        if m == s+"_":
            return ""
        return m

        