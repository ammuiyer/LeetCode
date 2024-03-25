class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        currMax = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currMax = max(prices[right]-prices[left], currMax)
            else:
                left=right
            right+=1
        return currMax


            