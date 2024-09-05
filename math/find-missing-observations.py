class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ret = []
        currsum = sum(rolls)
        goal = (mean*(len(rolls)+n)-currsum)
        if goal/6 > n or goal<0:
            return []
        else:
            a = goal//n
            rem = goal - a*n
            # print(goal, a, rem)
            for i in range(n):
                ret.append(a)
            x = 0
            while rem>0:
                if ret[x]<6:
                    ret[x]+=1
                x+=1
                rem-=1
            
                
        return ret
        