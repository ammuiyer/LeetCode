class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i]=="(":
                stack.append(("(", i))
            if s[i]==")":
                if len(stack)==0:
                    s = s[:i] + s[i+1:]
                    #print(s)
                    i-=1
                else:
                    stack.pop()
            i+=1
            #print(s)
        shift = 0
        if len(stack)>0:
            for item in stack:
                 s = s[:(item[1]-shift)] + s[(item[1]-shift)+1:]
                 shift+=1
                 #print(s, item)
            
        return s


