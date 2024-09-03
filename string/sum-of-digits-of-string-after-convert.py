class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new = 0
        p = 1
        for x in s:
            new = new*p + (ord(x)-96)
            p*=10


        ret = 0
        for i in range(k):
            ret = 0
            while new>0:
                ret+=new%10
                new=new//10
            #print(ret)
            new = ret
            

        return ret
        
        
        