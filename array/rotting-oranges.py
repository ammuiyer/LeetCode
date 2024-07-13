class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        time = 0
        cont1 = False
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    cont1 = True
                    if (i==len(grid)-1 or grid[i+1][j]==0) and (i==0 or grid[i-1][j]==0) and (j==len(grid[0])-1 or grid[i][j+1]==0) and (j==0 or grid[i][j-1]==0):
                        return -1
                if grid[i][j]==2:
                    q.append((i,j, 0))
        visited = set()
        if len(q)==0 and cont1:
            return -1
        while q:
            i, j, t = q.pop(0)
            if (i,j) not in visited:
                #explore
                if i<len(grid)-1 and grid[i+1][j]==1:
                    grid[i+1][j]=2
                    if (i+1, j) not in visited:
                        q.append((i+1, j, t+1))
                        time = t+1
                if j<len(grid[0])-1 and grid[i][j+1]==1:
                    grid[i][j+1]=2
                    if (i, j+1) not in visited:
                        q.append((i, j+1, t+1))
                        time = t+1
                if i>0 and grid[i-1][j]==1:
                    grid[i-1][j]=2
                    if (i-1, j) not in visited:
                        q.append((i-1, j, t+1))
                        time = t+1
                if j>0 and grid[i][j-1]==1:
                    grid[i][j-1]=2
                    print(grid)
                    if (i, j-1) not in visited:
                        q.append((i, j-1, t+1))
                        time = t+1
            visited.add((i,j))
            #print(i, j, t)
        #print(grid)
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return time
