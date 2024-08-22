class Solution:
    def findComplement(self, num: int) -> int:
        
        return int(num^(2**(len(bin(num)[2:]))-1))
        