class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums.sort(reverse=True))
        orig = len(nums)
        mid = floor(len(nums)/2)
        place = 0
        #print(nums)
        l = len(nums)
        i = mid
        while i < len(nums):
            #print(nums, i)
            nums.insert(place, nums[i])
            i+=2
            place+=2
        while len(nums)>orig:
            nums.pop()
        
        


        