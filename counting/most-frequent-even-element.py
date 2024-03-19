class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        currMax = [1, -1]
        i = 0
        if len(nums)>0 and nums[0]%2==0:
            currMax = [1, nums[0]]
        nums.sort(reverse=True)
        
        fre = 1
        
        while i < len(nums):
            
            if nums[i]%2 == 0 and i > 0 and nums[i]==nums[i-1]:
                fre+=1
            else:
                fre = 1
            if fre>=currMax[0] and nums[i]%2==0:
                    currMax[0] = fre
                    currMax[1] = nums[i]

            
            i+=1
        return currMax[1]

                

        