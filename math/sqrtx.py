class Solution:
    def mySqrt(self, x: int) -> int:
        
        l,m,h=1,x//2, x
        print(m)
        if x == 1:
            return 1
        while(l<h):
            p = m*m
            if p>x:
                h = m
                m = (l+h)//2 
            if p<x:
                l = m
                m = (l+h)//2 + 1
            if p==x:
                return m
            if (m-1)*(m-1)<x and m*m>x:
                return m-1
        return m

        