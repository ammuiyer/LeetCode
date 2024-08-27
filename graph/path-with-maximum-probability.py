class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        #bfs
        q = []
        q.append([start_node, 1])
        visited = set()
        visited.add(start_node)
        ma = 0
        while q:
            print(q)
            currnode, currweight = q.pop(0)
            if currnode==end_node:
                ma = max(ma, currweight)
            else:
                for i in range(0, len(edges)):
                    edge = edges[i]
                    if edge[0] == currnode:
                        q.append([edge[1], currweight*(succProb[i])])
                            #q.sort(key=lambda x:x[1])
                           
                            
        return ma
                
                    

        