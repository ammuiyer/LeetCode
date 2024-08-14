class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi = abs(nums[-1]-nums[0])
        def count(dist):
            count, i, j = 0, 0, 0
            while i < len(nums) or j < len(nums):
                while j < len(nums) and nums[j] - nums[i] <= dist:
                    j += 1
                count += j - i - 1
                i += 1
            return count>=k
        low = 0
        high = mi
        while(low<high):
            mid = low+(high-low)//2
            if not count(mid):
                #go up
                low = mid+1
            else:
                high = mid
        return low


