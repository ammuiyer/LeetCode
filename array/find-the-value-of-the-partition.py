class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        dist = inf
        for i in range(0, len(nums)-1):
            if (nums[i+1]-nums[i]) < dist:
                dist = nums[i+1]-nums[i]
        return dist
        #mid = len(nums)//2
        #return min(nums[mid]-nums[mid-1], nums[mid+1]-nums[mid])
        # a1 = []
        # a2 = []
        # flag = 0
        # for num in nums:
        #     if flag == 0:
        #         #add to max array
        #         a1.append(num)
        #         flag = 1
        #     else:
        #         #add to min array
        #         a2.append(num)
        #         flag = 0

        # return mx-mn
        