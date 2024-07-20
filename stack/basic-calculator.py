class Solution:
    def calculate(self, s: str) -> int:
        def ev(exp: str):
            exp = exp.replace(" ", "")
            exp = exp.replace("+-", "-")
            exp = exp.replace("--", "+")
            if "+" not in exp and "-" not in exp:
                return str(int(exp))
            l = 0
            currnum = exp[0]
            i = 1
            while i<len(exp) and exp[i]!="+" and exp[i]!="-":
                currnum+=exp[i]
                i+=1
            l = int(currnum)
            if i==len(exp):
                return str(l)
            currnum = ""
            curr_opr = exp[i]
            i+=1
            while i<len(exp):
                if exp[i]!="+" and exp[i]!="-":
                    currnum+=exp[i]
                else:
                    if curr_opr == "-":
                        l = l-int(currnum)
                    else:
                        l=l+int(currnum)
                    currnum=""
                    curr_opr = exp[i]
                i+=1
            if curr_opr == "-":
                    l = l-int(currnum)
            else:
                    l=l+int(currnum)
            return str(l)
        
        #print(ev("1"))
        
        stack = []
        i = 0
        #print("please")
        s=s.replace(" ", "")
        while i<len(s):
            if s[i]!=")":
                stack.append(s[i])
                #print(stack)
            else:
                currstr = ""
                while stack[-1]!="(":
                    currstr = stack.pop(-1) + currstr
                    #print(currstr)
                stack.pop(-1)
                stack.append(ev(currstr))
                #print(stack)
            i+=1
        if len(s)==1:
            #print("hello")
            return int(s)
        #print(stack)
        if len(stack)==1:
            return int(stack[0])
        #print(stack)
        return int(ev("".join(stack)))
        