class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0, 10:0, 20:0}
        for b in bills:
            d[b]+=1    
            
            if b==10:
                if d[5]>=1:
                    d[5]-=1
                else:
                    return False
            if b==20:
                if d[10]>=1 and d[5]>=1:
                    d[10]-=1
                    d[5]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
        return True
                   
        