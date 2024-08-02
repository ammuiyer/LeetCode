class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        ma = count = sum(nums[:ones])
        for i in range(ones, ones+len(nums)):
            count+= nums[i%len(nums)] # for circularness
            count-= nums[(i-ones+len(nums))%len(nums)]
            ma = max(ma, count)
        return ones-ma


    
        