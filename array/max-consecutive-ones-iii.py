class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0
        leftptr = 0
        rightptr = 0
        currMax = 0
        currK = 0
        total = 0
        while(rightptr < len(nums)):
            while(currK <= k and rightptr < len(nums)): 
                if nums[rightptr] == 1:
                    total+=1
                    rightptr+=1
                else:
                    if currK == k:
                         break

                    currK+=1
                    total+=1
                    rightptr+=1
            if total>currMax:
                currMax = total
            if rightptr == len(nums):
                break
            while(nums[leftptr]==1):
                total-=1
                leftptr+=1
            total-=1
            leftptr+=1
            currK-=1
        return currMax
            
