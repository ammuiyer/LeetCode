class Solution:
    def climbStairs(self, n: int) -> int:
        M = [1, 2]
        for i in range(2, n):
            M.append(M[i-1] + M[i-2])
        return M[n-1]


        