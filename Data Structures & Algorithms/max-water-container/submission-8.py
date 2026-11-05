class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        capacity = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            capacity = max(capacity, area)
            if heights[left] < heights[right]:
                previous_height = heights[left]
                left += 1
                while left < right and heights[left] <= previous_height:
                    left += 1
            else:
                previous_height = heights[right]
                right -= 1
                while left < right and heights[right] <= previous_height:
                    right -= 1
        return capacity