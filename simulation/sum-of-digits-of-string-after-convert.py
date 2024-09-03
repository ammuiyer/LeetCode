class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new = ""
        for x in s:
            #print((ord(x)-96))
            new += str(ord(x)-96)

        #print(new)
        new = int(new)
        ret = 0
        for i in range(k):
            ret = 0
            while new>0:
                ret+=new%10
                new=new//10
            #print(ret)
            new = ret
            

        return ret
        
        
        