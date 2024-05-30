class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        mi = inf
        for i in range(n-1, -1, -1):
            if nums[i]<=mi: 
                mi=nums[i]
            else:
                l=i
        r=-1
        ma = -inf
        for i in range(n):
            if nums[i]>=ma:
                ma=nums[i]
        
            else:
                r=i
            
        return r-l+1
    
        