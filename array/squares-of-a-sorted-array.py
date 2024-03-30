class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftptr = 0
        rightptr = len(nums)-1
        ret = []
        while(leftptr <= rightptr):
            if abs(nums[rightptr])>abs(nums[leftptr]):
                ret.append(nums[rightptr]**2)
                rightptr-=1
            else:
                ret.append(nums[leftptr]**2)
                leftptr+=1
        return [ret[i] for i in range(len(ret)-1, -1, -1)]