class Solution:
    def checkValidString(self, s: str) -> bool:
        starcount = 0
        count = 0
        for x in s:
            if x == ")":
                count-=1
                if count+starcount<0:
                    return False
            if x=="(":
                count+=1
            if x=="*":
                starcount+=1
        if not abs(count)<=starcount:
            return False
        starcount = 0
        count = 0
        for i in range(len(s) - 1, -1, -1):
            x = s[i]
            if x == ")":
                count-=1
            if x=="(":
                count+=1
                if count > starcount:
                    return False
            if x=="*":
                starcount+=1
        if abs(count)<=starcount:
            return True
        else:
            return False