class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rSum = []
        currSum = 0
        for num in nums:
            currSum+=num
            rSum.append(currSum)
        return rSum