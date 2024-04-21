class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        q = [source]
        visited = set()
        visited.add(source)
        d = collections.defaultdict(list)
        for thing in edges:
            d[thing[0]].append(thing[1])
            d[thing[1]].append(thing[0])
        # if destination<source:
        #     destination, source = source, destination
        while q:
            curr = q.pop()
            if curr == destination:
                return True
            #explore curr's neighbors
            for neighbor in d[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return False
        