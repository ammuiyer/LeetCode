class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit += prices[r] - prices[l]
            l += 1
            r += 1
        return profit