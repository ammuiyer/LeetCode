class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      #first find list of all starting letter indices
        starting_positions = []
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    starting_positions.append([i,j])
        if len(starting_positions)==0:
            return False
        path = set()
        def dfs(r, c, i):
            if i==len(word):
                return True
            if r < 0 or c < 0 or r>=len(board) or c>=len(board[0]) or word[i]!=board[r][c] or (r, c) in path:
                return False
            path.add((r,c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
            path.remove((r,c))
            return res
        for pos in starting_positions:
            print(pos[0], pos[1])
            if dfs(pos[0], pos[1], 0):
                return True
        return False
