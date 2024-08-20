class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #take one or two piles each tiem
        dp = {}
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]
        def recur(index, m):
            if index >= len(piles):
                return 0
            if index + 2*m >=len(piles):
                return piles[index]
            if (m, index) in dp: 
                return dp[(m, index)]
            res = 0
            for x in range(1, 2 * m + 1):
                if index + x >= len(piles):  
                    break
                take = piles[index] - piles[index + x]
                res = max(res, take + piles[index + x] - recur(index + x, max(m, x)))
            dp[(m, index)] = res
            return res

        return recur(0, 1)