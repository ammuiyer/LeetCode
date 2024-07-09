class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, len(height)-1
        total = 0
        leftmax, rightmax = height[lmax], height[rmax]
        while (lmax < rmax):
            if height[lmax]<=height[rmax]:
                lmax+=1
                leftmax = max(leftmax, height[lmax])
                if height[lmax]<min(leftmax, rightmax):
                    total+=min(leftmax, rightmax) - height[lmax]
            else:
                rmax-=1
                rightmax = max(rightmax, height[rmax])
                if height[rmax]<min(leftmax, rightmax):
                    total+=min(leftmax, rightmax) - height[rmax]
            print(lmax, rmax, total)
        return total