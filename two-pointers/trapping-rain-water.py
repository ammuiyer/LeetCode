class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        total_water = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        while (left < right):
            if (max_left <= max_right):
                if max_left - height[left] > 0:
                    total_water += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                if max_right - height[right] > 0:
                    total_water += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        
        return total_water
        