class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        currMax = max(nums[0], nums[1])
        best = [nums[0]]
        best.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            newVal = max(best[i-1], best[i-2]+nums[i])
            best.append(newVal) 
            if newVal > currMax:
                currMax = newVal
        return currMax

        