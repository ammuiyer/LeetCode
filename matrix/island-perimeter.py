class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        per = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    per+=4
                    if i<len(grid)-1 and grid[i+1][j]==1:
                        per-=2
                    if j<len(grid[0])-1 and grid[i][j+1]==1:
                        per-=2
                
        return per


        