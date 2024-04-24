class Solution:
    def tribonacci(self, n: int) -> int:
        vals = [-1]*38

        vals[0], vals[1], vals[2] = 0, 1, 1
        for i in range(3, 38):
            vals[i]=vals[i-1]+vals[i-2]+vals[i-3]
        return vals[n]
        