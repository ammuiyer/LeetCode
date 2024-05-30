class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while (len(t)>0 and t[0]=='#'):
            t = t[1:]
        while (len(s)>0 and s[0]=='#'):
            s = s[1:]
        i=0
        l = len(s)
        while i<l:
            if s[i]=='#':
                s = s[:i-1]+s[i+1:]
                if i!=0:
                    i = i-2 if i-2>=0 else 0
                #print(s, i)
            i+=1
            l = len(s)
        i=0
        l = len(t)
        while i<l:
            if t[i]=='#':
                t = t[:i-1]+t[i+1:]
                if i!=0:
                    i = i-2 if i-2>=0 else 0
                #print(t, i)
            i+=1
            l = len(t)
        while (len(t)>0 and t[0]=='#'):
            t = t[1:]
        while (len(s)>0 and s[0]=='#'):
            s = s[1:]
        return s==t