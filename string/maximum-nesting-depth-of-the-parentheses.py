class Solution:
    def maxDepth(self, s: str) -> int:
            m = 0
            # r, l = 0, 0
            # for x in s:
            #     if x == "(":
            #         l+=1
            #     elif x==")":
            #         r+=1
            #     else: 
            #         return False
            #     if r>l:
            #         return False
            count_l = 0
            for x in s:
                if x == "(":
                    count_l+=1
                    m = max(m, count_l)
                if x == ")":
                    count_l-=1
            return m


        