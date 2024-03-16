class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-1] * 1001
        dp[0] = 0
        for num in nums:
            for i in range(target - num, -1, -1):
                if dp[i] >= 0:
                    dp[i + num] = max(dp[i + num], dp[i] + 1)
        return dp[target]
                
        