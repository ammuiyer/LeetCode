class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = [nums[0]]
        ma, mi = nums[0], m[0]
        for num in nums[1:]:
            m.append(m[-1]+num)
        
        for i in range(1, len(m)):
            ma = max(ma, m[i], m[i]-mi)
            mi = min(mi, m[i])

        return ma

        