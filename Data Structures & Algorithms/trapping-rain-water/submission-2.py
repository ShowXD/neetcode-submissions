class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if len(height) < 3:
            return result
        heighest_index = height.index(max(height))

        left_heightest = height[0]
        for i in range(1, heighest_index):  # 左側最高
            left_heightest = max(height[i], left_heightest)
            result += left_heightest - height[i]
        
        right_heighest = height[-1]
        for i in range(len(height) - 2, heighest_index, -1):  # 右側最高
            right_heighest = max(height[i], right_heighest)
            result += right_heighest - height[i]

        return result