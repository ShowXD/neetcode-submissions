class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if len(height) < 3:
            return result
        left = 1
        right = len(height) - 2
        left_max = height[0]
        right_max = height[len(height) - 1]

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, height[left])
                water = left_max - height[left]
                result += water
                left += 1
            else:
                right_max = max(right_max, height[right])
                water = right_max - height[right]
                result += water
                right -= 1

        return result