class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        l=len(grid)
        for i in range(1,l):
            temp =  sorted(grid[i-1])
            for j in range(l):
                if grid[i-1][j] == temp[0]:
                    grid[i][j] += temp[1]
                else:
                    grid[i][j] += temp[0]
        return min(grid[-1])