class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(n, idx, visited, stones):
            visited[idx] = True
            for i in range(n):
                if not visited[i]:
                    if stones[idx][0] == stones[i][0]:
                        dfs(n, i, visited, stones)
                    if stones[idx][1] == stones[i][1]:
                        dfs(n, i, visited, stones)
        n = len(stones)
        group = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                group += 1
                dfs(n, i, visited, stones)
        return n - group 