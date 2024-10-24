class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        L=len(grid)
        if grid[0][0]==1 or grid[L-1][L-1]==1:  return -1
        visited={}

        
        def dfs(i,j):
            if i<0 or i>=L or j<0 or j>=L or grid[i][j]==1:
                return float('inf')
            if (i,j) == (L-1,L-1):
                return 1
            else:
                directions=((1,0),(0,1),(1,1),(1,-1))
                directions=((1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1))
                val=float('inf')
                for dr, dc in directions:
                    if (i+dr,j+dc) not in visited:
                        visited[(i,j)]=1
                        val=min(val,dfs(i+dr,j+dc))
                        visited.pop((i,j))          #the important line that other DFS solutions are missing
                return 1+val
        visited[(0,0)]=1
        ans=dfs(0,0)
        return ans if ans != float('inf') else -1
					