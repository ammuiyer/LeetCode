class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        #do bfs w a q
        q = [(x, 0)]
        visited = {}
        while True:
            #do all ops on a thing 
            curr, layer = q.pop(0)
            if curr == y:
                return layer
            if curr%11==0 and curr/11 not in visited:
                q.append((curr/11, layer+1))
            if curr%5==0 and curr/5 not in visited:
                q.append((curr/5, layer+1))
            if curr-1 not in visited:
                q.append((curr-1, layer+1))
            if curr+1 not in visited:
                q.append((curr+1, layer+1))
            visited[curr] = 1
        
            
            
            

        