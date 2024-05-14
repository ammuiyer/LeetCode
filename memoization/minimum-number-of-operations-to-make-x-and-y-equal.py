class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        #do bfs w a q
        q = [x]
        layer = 0
        visited = set()
        while q:
            #do all ops on a thing 
            currLen = len(q)
            for i in range(currLen):
                curr = q.pop(0)
                if curr == y:
                    return layer
                if curr%11==0 and curr/11 not in visited:
                    q.append(curr/11)
                if curr%5==0 and curr/5 not in visited:
                    q.append(curr/5)
                if curr>1 and curr-1 not in visited:
                    q.append(curr-1)
                if curr+1 not in visited:
                    q.append(curr+1)
                visited.add(curr)
            layer+=1
        
        
            
            
            

        