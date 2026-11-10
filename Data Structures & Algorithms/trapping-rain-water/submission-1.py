class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if len(height) < 3:
            return 0
        heighest = max(height)
        heighest_index = height.index(heighest)

        left_heightest = height[0]
        for i in range(1, heighest_index):  # 左側最高
            left_heightest = max(height[i], left_heightest)
            result += left_heightest - height[i]
        
        right_heighest = height[len(height) - 1]
        for i in range(len(height) - 2, heighest_index, -1):  # 右側最高
            right_heighest = max(height[i], right_heighest)
            result += right_heighest - height[i]

        return result