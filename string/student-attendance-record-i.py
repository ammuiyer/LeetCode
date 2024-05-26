class Solution:
    def checkRecord(self, s: str) -> bool:
        countL = 0
        countA = 0
        for x in s:
            if x=="L":
                countL+=1
                if countL>2:
                    return False
            else:
                countL=0
            if x=="A":
                countA+=1
                if countA>=2:
                    return False
            
        return True
        