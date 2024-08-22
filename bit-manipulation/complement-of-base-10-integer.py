class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(n^(2**(len(bin(n)[2:]))-1))
        