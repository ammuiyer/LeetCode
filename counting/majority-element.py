class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count==0:
                m = nums[i]
            if nums[i]==m:
                count+=1
            else:
                count-=1
        return m
        

