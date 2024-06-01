class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, m, score = 0, 0, 0
        r = len(tokens)-1
        while(l<=r):
            #print(l, r, power, score)
            if tokens[l]>power and score==0:
                #cannot play anything just quit
                return m
            if tokens[l]<=power:
                score+=1
                m = max(m, score)
                power-=tokens[l]
                l+=1
            else:
                #play right
                score-=1
                power+=tokens[r]
                r-=1
            
        return m

            




        