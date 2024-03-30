class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid = 0, 0
        right = len(nums)-1
        while mid <= right:
            if nums[mid]==0:
                #swap w left
                nums[mid], nums[left] = nums[left], nums[mid]
                left+=1
            if nums[mid]==2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right-=1
            else:
                mid+=1

            
