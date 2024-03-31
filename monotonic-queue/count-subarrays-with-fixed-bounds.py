class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # start has to be bigger than bad
        # start - bad = number to add
        # start is the min(index(minK), index(maxK))
        bad = -1
        mi = -1
        ma = -1
        numToAdd = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i]>maxK or nums[i]<minK:
                bad = i
            if nums[i]==minK:
                mi = i
            if nums[i]==maxK:
                ma = i
            start = min(mi, ma)
            if start > bad and mi > bad and ma > bad:
                # if bad != -1:
                #     numToAdd = start - bad
                numToAdd = start - bad
                count += numToAdd
        return count
        
                    
        