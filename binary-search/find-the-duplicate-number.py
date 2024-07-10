class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        #print(nums[slow], nums[fast])
        slow = nums[slow]
        fast = nums[nums[fast]]
        while(slow!=fast):
            print(slow, fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast!=slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow