class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        maxarea = 0
        while left < right:
            maxarea = max(maxarea, min(heights[left],heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1    
        return maxarea
            