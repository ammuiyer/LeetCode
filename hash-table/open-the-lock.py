class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def nexts(lock):
            res = []
            for i in range( 4):
                up = str((int(lock[i])+1)%10)
                down = str((int(lock[i])+9)%10)
                res.append(lock[:i]+up+lock[i+1:])
                res.append(lock[:i]+down+lock[i+1:])
            return res
        q = [("0000", 0)]
        visited = set(deadends)
        while q:
            lock, turns = q.pop(0)
            if lock==target:
                return turns
            else:
                for n in nexts(lock):
                    if n not in visited:
                        q.append((n, turns+1))
                        visited.add(n)
        return -1
