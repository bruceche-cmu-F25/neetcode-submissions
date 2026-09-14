class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        left = 0
        right = len(heights) - 1
        mostwater = 0
        while left < right:
            minh = min(heights[left], heights[right])
            dis = right -left
            mostwater = max(minh * dis, mostwater)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return mostwater