class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []

        def backtrack(curr, pos, tar):
            if tar==0:
                ret.append(curr.copy())
            if tar<=0: #if the target is negative and u fail to make a valid combo
                return
            else:
                prev = -1
                for i in range(pos, len(candidates)):
                    if candidates[i]==prev:
                        continue
                    curr.append(candidates[i])
                    
                    backtrack(curr, i+1, tar-candidates[i])
                    curr.pop()
                    prev=candidates[i]

        backtrack([], 0, target)
        return ret
            



        