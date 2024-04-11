class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count = 0
        stack = [num[0]]
        if len(num)==1 and k==1:
            return "0"
        for c in num[1:]:
            #print(stack)
            while count<k and stack and c<stack[-1]:
                stack.pop()
                count+=1
            stack.append(c)
        while count<k:
            stack.pop()
            count+=1
        retstr = ""
        while stack and stack[0]=="0":
            stack.pop(0)
        for x in stack:
            retstr+=x
        if retstr=="":
            return "0"
        return retstr
        