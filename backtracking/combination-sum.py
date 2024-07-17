class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        M = []
        M.append([[]])
        for i in range(1, target+1):
            M.append([])
        #print(M)
        for i in range(1, target+1):
            #print(i, M[i])
            for c in candidates:
                if i-c>=0:
                    #print("i minus c is ")
                    #print(i, c, i-c)
                    #print(M[i-c])
                    for way in M[i-c]:
                        waycopy = [t for t in way]
                        waycopy.append(c)
                        waycopy.sort()
                        if waycopy not in M[i]:
                            M[i].append(waycopy)                   
            #print(i, M[i])
        #print(M)
        return M[target]
        