class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left = right = 1
        for i in range(n):
            result[i] *= left
            result[n - i - 1] *= right
            left *= nums[i]
            right *= nums[n - i - 1]
        return result